"""Valida integridade de arquivos, vínculos e pares de cor, sem dependências."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re

ROOT = Path(__file__).resolve().parents[1]

class Document(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids, self.links, self.references = [], [], []
        self.h1 = 0
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        if tag == 'h1':
            self.h1 += 1
        for key in ('src', 'href'):
            if key in attrs:
                self.links.append(attrs[key])
        for key in ('for', 'aria-controls', 'aria-labelledby', 'aria-describedby'):
            self.references.extend(attrs.get(key, '').split())

html_files = [ROOT/'index.html', ROOT/'design-system/index.html', ROOT/'examples/email.html']
for path in html_files:
    doc = Document(path.read_text())
    assert len(doc.ids) == len(set(doc.ids)), f'IDs duplicados em {path}'
    assert set(doc.references) <= set(doc.ids), f'Referência ARIA/label inválida em {path}'
    if path.name != 'index.html' or path.parent.name == 'design-system':
        assert doc.h1 == 1, f'H1 ausente/duplicado em {path}'
    for link in doc.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        target = (path.parent/unquote(url.path)).resolve() if url.path else path
        assert target.is_file(), f'Asset ou link ausente: {path}: {link}'
        if url.fragment and target.suffix == '.html':
            assert url.fragment in Document(target.read_text()).ids, f'Âncora inválida: {link}'

css = (ROOT/'design-system/tokens.css').read_text()
blocks = {}
for theme, selector in [('light', ':root'), ('dark', '.dark')]:
    block = re.search(re.escape(selector)+r'\s*\{(.*?)\}', css, re.S).group(1)
    blocks[theme] = dict(re.findall(r'--([\w-]+):\s*(#[0-9a-fA-F]{6});', block))
assert set(blocks['light']) - {'brand-blue', 'brand-cyan', 'brand-teal'} == set(blocks['dark']), 'Tokens semânticos incompletos entre temas'
blocks['dark'] = {**blocks['light'], **blocks['dark']}

def luminance(color):
    values = [int(color[i:i+2], 16)/255 for i in (1, 3, 5)]
    rgb = [v/12.92 if v <= .04045 else ((v+.055)/1.055)**2.4 for v in values]
    return sum(v*w for v,w in zip(rgb, (.2126, .7152, .0722)))

def contrast(a, b):
    high, low = sorted((luminance(a), luminance(b)), reverse=True)
    return (high+.05)/(low+.05)

pairs = [('foreground','background'), ('foreground','card'), ('muted-foreground','background'), ('muted-foreground','card'), ('muted-foreground','muted'), ('card-foreground','card'), ('popover-foreground','popover'), ('primary-foreground','primary'), ('secondary-foreground','secondary'), ('accent-foreground','accent'), ('sidebar-foreground','sidebar'), ('sidebar-accent-foreground','sidebar-accent'), ('sidebar-primary-foreground','sidebar-primary')]
for state in ('success', 'warning', 'destructive', 'info'):
    pairs.extend([(state, state+'-subtle'), (state+'-foreground', state)])
measurements=[]
for theme, colors in blocks.items():
    for foreground, background in pairs:
        ratio = contrast(colors[foreground], colors[background])
        assert ratio >= 4.5, f'Contraste insuficiente em {theme} {foreground}/{background}: {ratio:.2f}'
        measurements.append((theme, foreground+'/'+background, ratio))
    for foreground in ('input','ring'):
        for background in ('background','card'):
            ratio=contrast(colors[foreground],colors[background])
            assert ratio >= 3, f'Controle/foco sem contraste: {theme} {foreground}/{background}: {ratio:.2f}'
            measurements.append((theme, foreground+'/'+background, ratio))
for foreground, background in [('#102c3d','#29abe2'),('#153c40','#65c8d0'),('#ffffff','#2423d6'),('#ffffff','#1d1cae'),('#18153b','#c0bfff'),('#18153b','#9796f0'),('#e7e7ff','#2d2cff')]:
    ratio=contrast(foreground, background)
    assert ratio >= 4.5, f'Contraste de marca/estado insuficiente: {ratio:.2f}'
    measurements.append(('brand',foreground+'/'+background,ratio))

all_css = '\n'.join((ROOT/'design-system'/p).read_text() for p in ('tokens.css','catalog.css','tailwind.css'))
defined = set(re.findall(r'--([\w-]+)\s*:', all_css))
used = set(re.findall(r'var\(--([\w-]+)\)', all_css))
assert used <= defined, f'Variáveis sem definição: {used-defined}'
for asset in re.findall(r'url\([\'"]?([^\)\'\"]+)', (ROOT/'design-system/catalog.css').read_text()):
    assert (ROOT/'design-system'/asset).is_file(), f'Fonte/asset ausente: {asset}'
for font in (ROOT/'design-system/assets/fonts').glob('*.ttf'):
    assert font.read_bytes()[:4] in (b'\x00\x01\x00\x00', b'OTTO'), f'Fonte inválida: {font}'
print(f'OK: 3 HTMLs; IDs, ARIA, âncoras e assets íntegros; {len(measurements)} pares de contraste aprovados.')
print(f'Menor contraste medido: {min(row[2] for row in measurements):.2f}:1 (inclui bordas/foco, limiar 3:1).')
if __name__ == '__main__':
    for theme in ('light', 'dark'):
        values = [row[2] for row in measurements if row[0] == theme and row[1] in [a+'/'+b for a,b in pairs]]
        print(f'Texto {theme}: mínimo {min(values):.2f}:1 (limiar 4.5:1).')
