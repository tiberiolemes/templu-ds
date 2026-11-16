# Verificação da entrega

Corte: 16/11/2026. Escopo: documentação, tokens, catálogo estático, fontes e ativos de marca. Nenhum backend ou aplicação existente foi modificado.

## Verificações concluídas

- `python3 scripts/check.py`: integridade dos três HTMLs, IDs únicos, relações ARIA/labels, âncoras locais, caminhos de imagens/fontes, definição de tokens e 57 pares de contraste.
- Contraste mínimo de texto nos pares testados: 4,97:1 no claro e 6,81:1 no escuro. Menor contraste de borda/foco: 3,27:1. Estados de hover/pressed e texto sobre cores de marca também incluídos. Esses números se referem aos pares explícitos no script, não a uma auditoria integral de toda a página.
- `node --check design-system/catalog.js`: sintaxe JavaScript aprovada.
- Revisão visual no Chrome disponível: desktop, emulação em 375 e 320 px e estados claro/escuro. Conferidos abertura, componentes, aplicação de site, composição de comunicação e e-mail móvel.
- Busca por “Marina” exibiu uma pessoa; busca sem correspondência mostrou vazio e contagem zero; limpar restaurou as três pessoas.
- Envio vazio mostrou erro e focou o campo. Inserção de “Beatriz Exemplo” acrescentou uma quarta linha com mensagem de temporariedade e sem reload. Recarregar restaurou os três exemplos e o estado inicial.
- Switch alternou a descrição e o estado acessível.
- Abas de aplicações alternaram por clique; seta direita levou Site a Comunicação.
- Dialog abriu com foco em Cancelar; Escape fechou e devolveu o foco ao botão Excluir exemplo.
- Ativos originais foram copiados sem redesenhar a assinatura. Poppins é local. E-mail usa PNG da assinatura para evitar depender de suporte a SVG em clientes de e-mail.
- Revisão mecânica Impeccable executada. Na versão inicial, os avisos sobre texto funcional pequeno motivaram elevar os textos a 12 px; a regra posterior de Tibério elevou o piso para 14 px em todos os contextos; a grade móvel recebeu correção de largura mínima. Avisos genéricos sobre padding de wrappers e containers não foram tratados como defeitos quando o filho já estabelece o espaço necessário.

## Limites da validação

O teste Playwright foi preparado, mas não chegou a executar: primeiro faltou a revisão de browser esperada pela versão disponível; usar o executável já instalado foi bloqueado pelo sandbox do macOS (`MachPortRendezvousServer / Permission denied`). A revisão real ocorreu pelo Chrome com controle de interface. Não se declara que a matriz automatizada completa passou.

O DevTools tentou conectar a seu manifesto de workspace e a CSP `connect-src 'none'` bloqueou a tentativa. Isso é uma restrição intencional do catálogo, que não precisa de conexões de dados. O favicon ausente observado no modelo de e-mail foi corrigido com o avatar local. O atributo autofocus foi retirado do dialog para não disparar processamento na abertura por fragmento; a ordem de foco nativa mantém Cancelar como primeira ação.

Não foram homologados leitor de tela, Gmail/Outlook, Safari/Firefox, dispositivos físicos, integração com uma versão instalada do shadcn, compilação Tailwind ou fluxos reais de pessoas/financeiro/permissões. Isso depende do projeto consumidor e está separado da entrega do design system.

## Risco e custo de execução

Risco principal: implementar os exemplos conceituais como se comprovassem módulos existentes. PRODUCT.md e o estudo dos materiais explicitam o limite. Os arquivos de origem com preço/trial conflitantes, retratos e e-book de terceiros não são redistribuídos.

As verificações são locais e proporcionais ao escopo. Na entrega inicial, nenhum workflow de CI, job, deploy ou GitHub Pages foi criado. A hospedagem solicitada depois usa a publicação nativa do Pages descrita abaixo.

## Reproduzir o check estático

```sh
python3 scripts/check.py
node --check design-system/catalog.js
```

Para revisar visualmente, executar o servidor conforme o README. O script estático não substitui a revisão de layout e interação.

## Hospedagem pelo GitHub Pages

Publicação solicitada por Tibério em 16/11/2026. Origem: raiz da branch `main`, modo de publicação nativo, com `.nojekyll`. A raiz redireciona para `design-system/index.html`, com caminhos relativos compatíveis com o prefixo `/templu-ds/`.

Antes da publicação, foram repetidos o check estático e a validação sintática do JavaScript. O build nativo do Pages é o único processo de publicação necessário; não foi criada uma suíte adicional de CI. O resultado do build e as respostas HTTP públicas devem ser conferidos a cada publicação.

## Atualização do mínimo tipográfico

Em 16/11/2026, Tibério definiu que nenhum texto do DS pode ficar abaixo de 14 px. A regra foi aplicada ao catálogo, componentes, legendas, código, estados, rodapés e e-mail, além da escala documentada e do mapeamento `text-xs`/`text-sm` para Tailwind.

A verificação local no Chromium mediu os tamanhos computados em 37 cenários: cinco larguras (320, 375, 768, 1024 e 1440 px), dois temas, os três painéis de aplicações, erro de campo, busca vazia, diálogo, toast e três larguras do e-mail. O menor tamanho encontrado foi 14 px, sem overflow horizontal da página, falhas de recursos ou erros de JavaScript. O check de integridade e os 57 pares de contraste continuam aprovados.
