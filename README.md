# Templu Design System

Uma linguagem moderna, clean e baseada em shadcn/ui para **sistema, site e comunicação da marca**. Identidade original preservada, Poppins, mínimo tipográfico de 14 px em todos os contextos, tokens semânticos e temas claro/escuro.

## Explorar

**[Abrir o Design System online](https://tiberiolemes.github.io/templu-ds/)**

- [Catálogo visual](design-system/index.html): marca, fundamentos, componentes interativos e aplicações.
- [Design system completo](DESIGN.md): decisões, regras, componentes, responsividade e acessibilidade.
- [Tokens CSS](design-system/tokens.css) e [mapeamento Tailwind v4](design-system/tailwind.css).
- [Guia de integração shadcn/ui](docs/shadcn.md).
- [Estudo dos materiais](docs/estudo-dos-materiais.md): fontes, inventário e divergências.
- [Modelo de e-mail](examples/email.html).
- [Verificação e limites](docs/validacao.md).

## Abrir localmente

Não requer npm, build ou instalação. Na raiz:

```sh
python3 -m http.server 4173 --bind 127.0.0.1
```

Abra http://127.0.0.1:4173/design-system/. O catálogo também abre diretamente por arquivo; a cópia para clipboard depende do contexto permitido pelo navegador e tem mensagem alternativa. Fontes e imagens são locais.

## O que esta entrega contém

Especificação e protótipo visual estático com CSS e JS nativos. Os exemplos demonstram o contrato visual shadcn; não são uma biblioteca React compilada nem módulos reais de um sistema. O guia orienta aplicar os tokens aos componentes shadcn do projeto consumidor, preservando sua acessibilidade.

Busca, formulário, alternância de tema, abas e confirmação funcionam localmente. A demonstração não envia dados e não mantém registros após recarregar. Use apenas nomes fictícios. Nenhum módulo, preço, trial, depoimento ou resultado comercial é apresentado como fato atual sem fonte.

A fonte primária da marca é o SVG original. O e-book encontrado nos materiais é da Prover e não comprova funcionalidades do Templu. Os materiais de origem continuam em `artefatos/templu` na pasta local; só os ativos necessários e este estudo são publicados.

## Publicação e direitos

Repositório: https://github.com/tiberiolemes/templu-ds.

O catálogo é publicado pelo GitHub Pages em https://tiberiolemes.github.io/templu-ds/, a partir da raiz da branch `main`. O arquivo `.nojekyll` mantém os arquivos estáticos sem processamento pelo Jekyll. Novas alterações em `main` acionam a publicação nativa do Pages; não há workflow personalizado nem suíte de CI neste repositório.

A marca e seus ativos pertencem aos respectivos titulares; não há concessão implícita de licença aberta para eles. Poppins é distribuída sob [SIL OFL 1.1](design-system/assets/fonts/OFL.txt). Fotografias, retratos de suporte, arquivo Illustrator e e-book de terceiros não são redistribuídos.
