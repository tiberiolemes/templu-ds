# Design system Templu

Versão 1.0 · 16 de novembro de 2026 · Sistema, site e comunicação

## Direção

Clareza para gerir. Proximidade para cuidar.

Uma interface limpa, precisa e humana. Branco e neutros frios criam espaço para a informação. O azul Templu orienta ações e seleção; ciano e turquesa conectam a interface à identidade original. Poppins, já usada nos e-mails, mantém a continuidade da marca. Componentes seguem o vocabulário shadcn/ui, sem ornamentos competindo com a tarefa.

Esta é uma proposta de design system. Preserva ativos originais e acrescenta regras de produto, acessibilidade e composição. Não constitui comprovação dos módulos atuais, reposicionamento comercial aprovado ou aplicação pronta para produção.

## Fontes e autoridade

| Elemento | Evidência | Decisão nesta entrega |
| --- | --- | --- |
| Nome e símbolo | SVG, PNGs e PDF da marca | Preservar integralmente |
| Azul #2D2CFF | `.st0` no SVG original | Referência digital principal |
| Ciano #29ABE2 e turquesa #65C8D0 | `.st1` e `.st5` no SVG | Apoio de marca; não estados de negócio |
| Poppins | HTML dos dois e-mails | Expandir para os três contextos |
| Azul mais sóbrio no PDF | Representação visual do PDF | Registrar como variação histórica; não substituir o SVG |
| Azul #0084FF | Botões de e-mail legados | Unificar novos CTAs no azul Templu |
| Superfícies, escala, raios, estados, dark | Não havia sistema documentado | Novas decisões propostas |

Inventário e divergências em [Estudo dos materiais](docs/estudo-dos-materiais.md). Arquivos executáveis de referência: [tokens](design-system/tokens.css) e [catálogo](design-system/index.html).

## Princípios

1. A informação vem antes da decoração. Evitar gradientes em telas de trabalho, sombras em cada bloco e excesso de cartões.
2. Uma ação principal por contexto. Destruição tem tratamento próprio e confirmação proporcional ao impacto.
3. Pessoas recebem linguagem respeitosa. Não inferir vínculo, inadimplência, consentimento ou identidade a partir de proxies visuais.
4. Cor tem função. A mesma cor representa a mesma intenção; texto, ícone e posição garantem significado além dela.
5. Sistema, site e comunicação compartilham os fundamentos, com densidade e escala adequadas a cada uso.

## Marca

Usar [templu.svg](design-system/assets/brand/templu.svg) em fundos claros e [templu-white.png](design-system/assets/brand/templu-white.png) em escuros. O SVG original foi copiado sem redesenho; ele é a fonte preferida para uso digital. O arquivo branco original é raster e não deve ser ampliado além de sua resolução útil. O avatar original serve para favicon e ícone de produto; não é uma fotografia de usuário.

O símbolo, conforme a explicação da marca, reúne pessoas de mãos dadas, oração, nuvem/céu e Trindade. A marca não precisa de cruzes, igrejas ou ícones religiosos adicionais na interface.

Regras propostas: largura mínima de 112 px para assinatura completa; ícone em 24–40 px; área livre ao redor equivalente a metade da altura do símbolo. Essas medidas são novas regras de aplicação, não afirmações de um manual legado. Não distorcer, girar, separar partes, trocar cores, aplicar sombra, recriar a palavra com Poppins ou usar sobre fotografia sem área de leitura protegida.

## Cores

### Marca

| Papel | Valor | Uso |
| --- | --- | --- |
| Azul Templu | `#2D2CFF` | Assinatura, CTA principal no claro, seleção |
| Azul hover | `#2423D6` | Hover das ações principais |
| Azul pressed | `#1D1CAE` | Pressed das ações principais |
| Ciano | `#29ABE2` | Apoio de identidade, gráficos com rótulos e contraste verificado |
| Turquesa | `#65C8D0` | Apoio, planos de marca e detalhes de composição |

Não usar branco em texto pequeno sobre ciano ou turquesa. Nesses fundos, usar texto escuro como no catálogo. Ciano e turquesa não significam automaticamente sucesso. No dark, `primary` passa a `#AAA9FF` com texto `#18153B`; a marca continua com as cores originais e usa a versão branca onde necessário.

### Tokens semânticos

[Tokens CSS](design-system/tokens.css) é a fonte executável. Não copiar hexadecimais por componente. Para neutros, interações e estados, usar os nomes abaixo. As cores de marca permanecem em `brand-*` e não mudam com o tema.

| Par / token | Claro | Escuro | Aplicação |
| --- | --- | --- | --- |
| `background` | #F7F8FA | #11131C | Canvas |
| `foreground` | #191B28 | #EEEEF5 | Texto principal |
| `card` | #FFFFFF | #191C28 | Painel |
| `muted` | #F0F1F5 | #232635 | Apoio |
| `muted-foreground` | #636779 | #AAAEC1 | Texto secundário e placeholder |
| `primary` | #2D2CFF | #AAA9FF | Ação principal |
| `primary-foreground` | #FFFFFF | #18153B | Texto na ação |
| `accent` | #EEEDFF | #2B2850 | Seleção / hover contextual |
| `accent-foreground` | #3022B9 | #C8C5FF | Texto na seleção |
| `border` | #E1E3EB | #333747 | Divisória decorativa |
| `input` | #85899B | #767D95 | Borda identificadora de controle |
| `ring` | #2D2CFF | #AAA9FF | Foco opaco |
| `success` | #166A4B | #78DCB2 | Sucesso confirmado |
| `warning` | #86520A | #F2CD7D | Atenção |
| `destructive` | #B42332 | #FF9AA5 | Erro e ação destrutiva |
| `info` | #165F88 | #8ED0F5 | Informação |

Estados usam pares `*-foreground` em preenchimentos sólidos e `*-subtle` com texto no token principal para mensagens suaves. Os tokens de sidebar, popover e cinco séries de gráfico estão definidos para ambos os temas. Não misturar significado de gráfico com significado de status. Gráficos precisam de rótulos, legenda e alternativa tabular; cor sozinha não diferencia séries.

## Tipografia

Poppins 400, 500, 600 e 700. Os arquivos locais e a licença ficam em `design-system/assets/fonts`; sem dependência de Google Fonts em runtime. Fallback: `ui-sans-serif, system-ui, sans-serif`. O logotipo é um desenho próprio e nunca usa esta pilha.

| Estilo | Tamanho / entrelinha | Peso | Uso |
| --- | --- | --- | --- |
| Display site | 48 / 56 px | 600 | Título principal, máximo de duas ou três linhas |
| Display mobile | 32 / 40 px | 600 | Até 767 px |
| H1 produto | 28 / 36 px | 600 | Título de página |
| H2 produto | 20 / 28 px | 600 | Seção |
| H3 produto | 16 / 24 px | 500–600 | Grupo |
| Corpo produto | 14 / 22 px | 400 | Tabelas e formulários reais |
| Corpo site e e-mail | 16 / 24–28 px | 400 | Leitura prolongada |
| Label | 12 / 18 px | 500 | Labels e metadados |
| Caption | 12 / 18 px | 400 | Informação complementar |

Usar rem com base de 16 px e respeitar zoom. Tracking de títulos entre -0.02em e -0.03em; corpo normal. Parágrafos de até 65–75 caracteres por linha. Valores financeiros alinhados à direita com `font-variant-numeric: tabular-nums`. Não diminuir texto operacional abaixo de 12 px. O mini produto do catálogo é uma maquete reduzida, não a escala final de uma aplicação.

## Espaço, forma e profundidade

Escala de espaço: 4, 8, 12, 16, 20, 24, 32, 40, 48 e 64 px. Entre ícone e label: 8 px; label e campo: 8 px; campos: 16–24 px; grupos: 24–32 px; seções de site: 64–96 px. Margens laterais: 16–24 px no mobile, 24–40 px no produto desktop.

Raios: 6 px pequeno, 8 px controles, 10 px base, 14 px painéis. Pills apenas para controles pequenos que precisem dessa forma, switches e avatares. Bordas de 1 px. Separadores leves não substituem as bordas de controle necessárias para identificação.

Painéis usam borda, sem sombra. Popovers usam `0 8px 24px` e dialog usa `0 20px 64px`; não empilhar borda e sombra forte. Overlays via portal ou top layer, sem recorte pelo overflow da tabela.

## Layout responsivo

| Contexto | Desktop | Tablet | Mobile |
| --- | --- | --- | --- |
| Sistema | Sidebar 240 px; conteúdo flexível | Sidebar compacta ou Sheet | Sheet com rótulo e foco; fluxo de uma coluna |
| Site | Container até 1200 px; grade de 12 colunas | 8 colunas | 4 colunas; margens de 24 px |
| Formulário | Até 720 px; 1–2 colunas por relação | 1–2 colunas | Uma coluna, label acima |
| Tabela | Toolbar, cabeçalho, ações contextualizadas | Priorizar colunas | Scroll local ou lista equivalente com todos os dados acessíveis |

Breakpoints de integração propostos: 640, 768, 1024 e 1280 px. Não definir experiências apenas por dispositivo: conferir conteúdo real, tradução, zoom e teclado. Um CTA não deve cobrir o conteúdo quando o teclado móvel abre.

O catálogo usa navegação lateral no desktop e leitura contínua por seções no mobile. A prévia reduzida omite a coluna Grupo no mobile como recurso de apresentação; uma tabela operacional deve oferecer acesso equivalente ao dado.

## Componentes

O [contrato shadcn](docs/shadcn.md) mapeia variantes, estados e integração. Reutilizar componentes gerados, em vez de recriar comportamentos acessíveis.

| Componente | Regra |
| --- | --- |
| Button | 40 px padrão; 32 px compacto em desktop; 44 px em superfícies de toque. Primário, secondary, outline, ghost, destructive e link |
| Input / Textarea | Label persistente, descrição e erro ligados por ID; altura mínima de 40 px; texto 14 px; validação próxima |
| Select / Combobox | Select para lista curta; Combobox quando a busca for útil; estado vazio e loading explícitos |
| Checkbox / Radio / Switch | Não intercambiar: seleção múltipla, escolha exclusiva e alternância de estado, respectivamente |
| Table / Data Table | Títulos claros, alinhamento, ordenação com `aria-sort`, seleção explícita, filtros e paginação quando necessários |
| Badge | Texto curto e significado estável; não simular botão se não houver ação |
| Tabs | Alterna painéis do mesmo contexto; setas/Home/End, `aria-selected` e foco móvel |
| Alert | Feedback persistente; problema, consequência e recuperação; sem depender só da cor |
| Sonner / toast | Resultado secundário; região live; não único lugar de erro crítico |
| Dialog / AlertDialog | Dialog para foco necessário; AlertDialog para consequências. Cancelar como foco inicial em destruição |
| Sheet | Navegação móvel ou tarefa lateral curta; restaurar foco e fechar por Escape |
| Tooltip | Ajuda complementar no hover e foco; nunca único rótulo ou instrução indispensável |
| Skeleton / Empty | Reserva de espaço e orientação. Não inventar valores durante carregamento |

### Estados obrigatórios

Todo controle prevê default, hover, foco, pressed/selected, disabled e loading quando aplicável. Em campos, também invalid e read-only. Em conjuntos de dados, loaded, empty, filtered-empty, loading, error e sem permissão.

Disabled mantém label legível e motivo próximo quando necessário. Loading preserva largura e label, usa `aria-busy` e evita envio duplicado; sempre sai de loading em sucesso ou erro. Não desabilitar permanentemente uma ação após falha. Skeleton não anuncia cada linha para leitores de tela.

Mensagens propostas: “Informe um nome para continuar”; “Não foi possível salvar. Seus dados continuam aqui”; “Nenhuma pessoa corresponde aos filtros”; “Você não tem permissão para visualizar estas informações”. Última mensagem não comprova autorização: o backend precisa negar os dados.

### Formulários e segurança

Submissões e ações de estado não recarregam a página: usar o mecanismo assíncrono do framework, preservar entrada em falhas, exibir erro inline e resultado confirmado pelo servidor. Validar também no servidor. Não converter visualmente uma ação em sucesso antes da confirmação real, especialmente em finanças.

Filiação religiosa, pedidos de oração, dados de menores e registros financeiros exigem definição real de permissões, minimização e retenção. Não os incluir em analytics, logs ou exemplos públicos. Não enviar senhas por e-mail. Recuperação deve levar a um fluxo com token expirável validado no backend, quando implementado. O catálogo usa apenas dados fictícios e renderiza texto livre com `textContent`.

## Movimento

120 ms para hover; 180 ms para alternância e abertura; easing `cubic-bezier(.16,1,.3,1)`. Movimento comunica estado. Sem entradas em cascata no produto. Respeitar `prefers-reduced-motion`; nenhuma informação pode depender da animação.

## Acessibilidade

Meta de implementação: WCAG 2.2 AA; não é uma declaração de conformidade de aplicação futura. Texto normal ≥4.5:1; texto grande e limites identificadores de controles ≥3:1. Foco de 2 px opaco e offset de 2–4 px, sem cobertura por header fixo. Não herdar automaticamente rings com baixa opacidade sem medir o contraste composto.

Operação integral por teclado; skip link; landmarks; um H1; hierarquia sem saltos; labels e nomes acessíveis. Tabelas com cabeçalhos; erros associados ao campo; ícones decorativos com `aria-hidden`. Modais contêm foco e devolvem ao disparador. Alvos de 44 px são o padrão de toque proposto, mesmo quando o desenho aparente é menor. Confirmar leitores de tela, zoom a 200% e reflow em 320 px na aplicação real.

## Três contextos

### Sistema

Modo operar: poucos planos, informação alinhada, sidebar clara e barra de ação contextual. Fotos apenas quando úteis à identificação e autorizadas. Ícones de produção: Lucide, tamanho 16–20 px e traço consistente. O catálogo usa um pequeno conjunto de geometrias inline autorais; não é uma distribuição Lucide nem substitui o pacote do produto.

### Site

Modo apresentar: mensagem principal curta, espaço generoso, marca íntegra e CTA claro. Prova real perto da alegação que sustenta. Evitar números, preços, depoimentos e módulos sem fonte atual. Fotografia deve ser real, autorizada e relevante ao cuidado com a comunidade; nenhuma imagem antiga tem direito de republicação presumido nesta entrega.

A composição “Mais tempo para estar perto” é uma proposta de mensagem, não promessa medida. Os exemplos do catálogo ilustram composição e não constituem uma landing page comercial final.

### Comunicação

Tom próximo, direto, acolhedor e respeitoso. Usar você para ações pessoais e sua comunidade para contexto coletivo. Evitar jargão técnico, urgência artificial e fala religiosa decorativa em mensagens de sistema.

Social: 1080×1350 px para retrato 4:5; margem de 80 px; uma ideia principal; marca completa com pelo menos 224 px de largura; título entre 72–104 px conforme a quantidade de texto; corpo 32–40 px; CTA apenas quando houver destino real. Azul sólido e pequenas áreas ciano/turquesa. A composição no catálogo é escalada proporcionalmente.

E-mail: largura de até 600 px, margem interna de 32 px desktop e 24 px mobile, corpo de 16/24 px, um CTA, fonte Arial de fallback, imagens com alt e tabelas de apresentação. O [modelo local](examples/email.html) é visual e não envia e-mail. Preservar placeholders e ligar a eventos reais antes de usar; QA em Gmail e Outlook ainda é necessário.

## Integração e governança

[Guia de integração](docs/shadcn.md). Atualizar tokens primeiro, depois componentes, depois superfícies. Registrar decisões novas e impacto em consumidores. Evitar um wrapper para cada componente: as variantes do próprio shadcn e tokens resolvem o tema.

Sem contrato de licença aberta para a marca. Os direitos dos ativos Templu continuam com seus titulares. As fontes seguem SIL OFL 1.1. Esta entrega não redistribui o e-book de terceiros, retratos de suporte ou arquivos editáveis originais.

Mudanças patch corrigem inconsistências sem mudar contrato; minor acrescenta variantes compatíveis; major altera significado, tipografia principal ou estrutura de tokens. Antes de release, verificar ambos os temas, mobile/desktop, teclado, contraste, estados, fontes e assets. Histórico e limites em [Validação](docs/validacao.md).
