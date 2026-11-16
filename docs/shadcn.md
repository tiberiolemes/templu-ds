# Integração shadcn/ui

O Templu é uma camada de identidade sobre tokens e componentes shadcn/ui. Este repositório entrega o contrato visual, CSS portável, catálogo estático e modelo de e-mail. Não contém uma biblioteca React compilada, backend ou pacote npm.

## Base técnica

A documentação oficial recomenda variáveis CSS semânticas e pares superfície/foreground. Os tokens preservam essa convenção e são sobrescritos por `.dark`. Referência verificada em 16/11/2026: [Theming](https://ui.shadcn.com/docs/theming), [Installation](https://ui.shadcn.com/docs/installation) e [Components](https://ui.shadcn.com/docs/components).

No projeto consumidor, inicializar shadcn de acordo com o framework real e manter `tailwind.cssVariables: true`. Escolher a base de primitivos suportada pelo projeto e mantê-la consistente; não misturar APIs de diferentes bases. Este DS não depende do nome de um preset.

A receita abaixo é para Tailwind v4. Se o consumidor usa v3, os mesmos tokens continuam válidos, mas o mapeamento deve ir ao `tailwind.config` em vez de `@theme inline`.

```css
/* globals.css: preservar imports gerados pelo projeto e pelo shadcn. */
@import "tailwindcss";
/* ...outros imports exigidos pela instalação escolhida... */
@import "./design-system/tokens.css";
@import "./design-system/tailwind.css";
```

Copiar os dois arquivos para o projeto, ou ajustar os caminhos. Carregar as fontes via @font-face, preservando os arquivos e a licença em `assets/fonts`. O mapeamento de `tailwind.css` não importa o CSS visual do catálogo.

Hexadecimais são valores CSS válidos para os tokens. Não envolver `var(--primary)` em `hsl()` ou `oklch()`: a variável já contém a cor inteira. Manter as classes semânticas, como `bg-background`, `text-muted-foreground`, `border-input` e `bg-primary`.

## Mínimo de 14 px

Todo texto do DS usa pelo menos 14 px, incluindo labels, legendas, badges, metadados, código e rodapés. `--font-size-min: .875rem` pressupõe a base de 16 px; não reduzir o tamanho da raiz nem escalar textos para contornar o mínimo.

O mapeamento de `tailwind.css` redefine `text-xs` e `text-sm` para o mesmo piso de 14 px e entrelinha de 22 px. Isso cobre usos de `text-xs` nos componentes shadcn gerados. Não adicionar classes arbitrárias abaixo desse piso. Textos de apoio continuam distintos por peso, cor e espaço. Referência de configuração: [font-size do Tailwind](https://tailwindcss.com/docs/font-size).

## Usar os componentes de origem

```tsx
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"

export function ExampleField() {
  return (
    <div className="grid gap-2">
      <Label htmlFor="name">Nome</Label>
      <Input id="name" aria-describedby="name-help" className="h-10 border-input" />
      <p id="name-help" className="text-sm text-muted-foreground">
        Informe o nome como a pessoa prefere ser chamada.
      </p>
      <Button type="button" className="h-10 rounded-md hover:bg-primary-hover active:bg-primary-active">
        Adicionar pessoa
      </Button>
    </div>
  )
}
```

O snippet ilustra a composição visual. A ação e a validação do formulário devem ser ligadas ao fluxo real do consumidor; ele não é um cadastro implementado.

## Contrato de variantes

| shadcn | Templu | Requisitos |
| --- | --- | --- |
| Button default | Primary | `bg-primary text-primary-foreground`, hover/active próprios; evitar opacidade que altere contraste sem medição |
| Button secondary | Apoio | `bg-secondary text-secondary-foreground` |
| Button outline | Contorno | `bg-card border-input text-foreground`; borda identificadora ≥3:1 |
| Button ghost | Contextual | Transparente; hover muted; foco opaco |
| Button destructive | Destrutivo | `bg-destructive text-destructive-foreground`; não depender de estilo upstream que omita o foreground |
| Badge secondary | Neutro | Texto de estado em fundo muted, sem tratar vínculo como sucesso |
| Badge semântico | Estado | `bg-success-subtle text-success`, equivalentes warning/info/destructive |
| Input / Select trigger | Campo | 40 px, 14 px, label persistente; `border-input`; mobile com alvo de 44 px |
| Card | Painel | Borda ou sombra, raio 14 px e padding 24 px; sem card dentro de card |
| Table / Data Table | Dados | 14 px; mínimo 14 px em metadados; célula de 48–56 px; cabeçalho 40 px |
| Sidebar | Navegação | Tokens `sidebar-*`; 240 px desktop; Sheet no mobile |
| Dialog / AlertDialog | Overlay | Raio 14 px; padding 24 px; backdrop; portal/top layer e restauração de foco |
| Tooltip / DropdownMenu / Popover | Contexto | Tokens popover, foco/teclado da base; não recortar por overflow |
| Tabs | Painéis | Seta esquerda/direita, Home/End, roving tabindex e relação tabpanel |
| Switch / Checkbox / RadioGroup | Escolhas | Nome acessível, estado programático e alvo de toque ampliado |
| Sonner / Alert | Feedback | Região live apropriada, descrição de falha e recuperação, sem expor dados sensíveis |

Não reimplementar a lógica de Dialog, Select e menus por motivo visual. Manter os primitivos de acessibilidade da base. Ajustar o foco gerado para um ring opaco de 2 px, por exemplo `focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2`, observando as classes já existentes e o utilitário de merge do projeto. Confirmar o estilo computado: classes concorrentes de opacidade podem prevalecer.

## Tema

O consumidor alterna `.dark` no elemento raiz por seu mecanismo existente. Respeitar preferência do usuário e evitar flash de tema; persistência e SSR dependem do framework real. O catálogo não usa localStorage e começa no tema claro; sua alternância vale apenas enquanto a página está aberta.

## Fluxo de implementação

1. Integrar tokens e fonte; renderizar os componentes já existentes.
2. Ajustar variantes do arquivo Button e bordas/rings dos campos, sem wrappers desnecessários.
3. Validar tabela, formulário, overlay, menu, vazio, erro e loading nos dois temas.
4. Conectar handlers assíncronos e estados reais; backend garante validação, autorização e isolamento.
5. Verificar contraste composto, toque, teclado, reflow e leitor de tela com a versão instalada.

Não instalar bibliotecas de gráficos ou de tabelas apenas para apresentar um exemplo. Quando o produto exigir ordenação, paginação ou charts, reutilizar a stack presente.
