# Estudo dos materiais Templu

Estudo local realizado em 16/11/2026. Foram inventariados 30 arquivos úteis: 24 imagens raster, 2 PDFs, 2 e-mails HTML, 1 SVG e 1 Illustrator. Arquivos `.DS_Store` foram desconsiderados. O AI foi identificado como fonte editável, sem auditoria de suas camadas internas. Não havia código de aplicação, package.json ou design system anterior.

## O que foi observado

### Marca e significado

O PDF explicativo tem 3 páginas: conceito do símbolo, simulação social e assinatura. O símbolo representa comunidade, pessoas de mãos dadas, oração, Trindade e nuvem/céu. SVG e PNGs confirmam a assinatura horizontal, nome em minúsculas e presença de azul, ciano e turquesa.

O SVG define `.st0 #2D2CFF`, `.st1 #29ABE2` e `.st5 #65C8D0`; contém também classes auxiliares do arquivo de origem. A existência de outras cores no stylesheet não comprova seu uso como paleta de marca. #2D2CFF é a âncora digital proposta por existir em arquivo vetorial reutilizável e ser coerente com as peças digitais. O PDF exibe azul mais sóbrio, sem uma especificação numérica comum a todos os arquivos. Não se concluiu que um arquivo seja uma atualização oficial do outro.

### Imagens e comunicação

As 24 imagens foram inspecionadas em prancha de contato; logos e peças principais também em tamanho individual. Os conjuntos se dividem em assinatura/ícone, explicação, aplicações sociais, fundos de ajuda, splashes de login e retratos de suporte. Os fundos históricos têm azul intenso, cortes curvos e símbolos ampliados. A proposta conserva as cores e simplifica o uso em telas operacionais; essas composições não viram fundo de tabelas ou formulários.

Os retratos são arquivos de suporte/persona, não prova de equipe ou depoimento. Não foram redistribuídos nem usados como membros de igreja. As fotografias de culto existentes não têm comprovação de direitos de republicação neste contexto e também não foram incorporadas.

### E-mails

Os dois HTMLs usam Poppins, tabelas de 600 px, azul de botão #0084FF, fundo #F9F9F9 e rodapé #151822. Isso oferece evidência de tipografia e estrutura, mas não de um sistema semântico consistente. Alguns links são placeholders e os assets dependem de URLs externas.

O modelo antigo de recuperação informa uma nova senha no corpo. Esse padrão não foi reproduzido: o DS especifica recuperação por link com token expirável validado pelo backend. O HTML histórico não foi alterado.

### E-book de terceiros

As 14 páginas foram extraídas para leitura de conteúdo. A capa e a identificação foram conferidas visualmente. O material é da Plataforma Prover/sistemaprover.com.br, produzido em 2021. Ele é útil apenas para entender tarefas administrativas do segmento. Não comprova módulos de pessoas, financeiro, pagamentos, infantil, grupos, eventos, transmissões, site ou app no Templu. Nenhum número, depoimento, condição ou funcionalidade dele foi adotado como verdade do produto.

### Condições comerciais divergentes

A simulação social mostra 14 dias e R$ 49,90; a thumbnail e o postlink mostram 7 dias. São condições históricas e conflitantes. O DS não declara preço, teste gratuito, quantidade de clientes ou resultado financeiro atual.

## Decisões novas propostas

- Poppins 400/500/600/700 como família comum para sistema, site e comunicação.
- Azul do SVG como âncora digital; neutros frios, dark e estados acessíveis derivados.
- Densidade operacional limpa, componentes com vocabulário shadcn e tokens portáveis.
- Site com escala maior e espaço para provas reais. Comunicação com uma ideia por peça.
- Sem redesenho de logotipo ou reprodução de conteúdo comercial não confirmado.

Essas decisões expandem o material existente; não são apresentadas como um manual original já aprovado.

## Inventário completo

Os caminhos abaixo são da pasta de origem local, não links para arquivos publicados. SHA-256 identifica o material estudado sem redistribuí-lo. A prancha de contato permanece em `.validation/assets.png`, excluída da publicação.

| Arquivo em artefatos/templu | Tipo | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| 01.png | PNG | 17184 | `ab2f1ad027d66460dffcc05a86ae5fa3b2f1e5161132e5f4b340ce9dec2c89b3` |
| 02.png | PNG | 52549 | `807a6e029973ab892fe7869d241ff4d2512150ff546f472155301f0121828a71` |
| 03.png | PNG | 272276 | `0616d9c1862e4127d2bc9f660a670765c0e61e9642eba667e17dca90248e8df4` |
| 1652732757276ebook-primeiros-passos-para-automatizar-a-gestao-da-sua-igreja.pdf | PDF | 7800982 | `7a0563b95e65492eb7cf73d55f8017b6b6fc717bf2ec2106d74f5373e5b808d8` |
| Amanda_Suporte - Menor.png | PNG | 156635 | `08d42bf4951371101e13f95c26f7d5b10f4e180cfab6e4711db749555e35534e` |
| Amanda_Suporte.png | PNG | 1191449 | `4b77c9640448e45f124ab8f8171690fbc366951f90b39c0b2d2c54cd9b9db130` |
| E-mails Transacionais/email_novaconta.html | HTML | 11971 | `5d8a3fde27d0824903f74369b7036856ae3dd1cb2a3d81608327b6b34c822f73` |
| E-mails Transacionais/email_recuperacaosenha.html | HTML | 9700 | `027fd52b2f03185c680bb30b735e4499d837769dfafb1c71884d9a69766d33e3` |
| Marca/Explicação da Marca - Templu.pdf | PDF | 1427433 | `af398829affb50edc067405400e5d3a56e0f6e4958a945ef4e11f53579bd9447` |
| Marca/Marca Templu-06.svg | SVG | 5718 | `367b6667626dbf78d5bc2f58a33a5e6dc2d0383f65a1bea024582f2a10a41089` |
| Marca/Marca Templu.ai | AI | 54961977 | `30f5b4baa2a216e3f4ee95f73bbb7fe1708362dd0e6d8080cb4f352f494c99b9` |
| Marca/avatar.png | PNG | 26234 | `ce1c324aeb8b6857cc6313045339cd08c1cbc6d909b557c5e4dabce99a52efe8` |
| Marca/templULogo_site.png | PNG | 5988 | `7c167f7923cd51ce33bca11718fa2da99f89f21585e2481e7a75145914f86cb1` |
| Marca/templu_thumb.png | PNG | 1142626 | `960427101d9a028fe05016f640481da6d5992d67594b0a4293075dcff1615a5d` |
| PNGs Web/02bg_central_de_Ajuda.jpg | JPG | 87928 | `19ab2980058424180c8e4e5a5caa0bf7e226dcb9bee86af366b35be9a5d2564f` |
| PNGs Web/03bg_central_de_Ajuda.jpg | JPG | 72452 | `b72acdef8ae1c7d607595d5eaf1c501ff214a2d7a84138076eca3dc36ef26344` |
| PNGs Web/04bg_central_de_Ajuda.jpg | JPG | 61008 | `f4141fabe4d822d31545835c81b0915dbba2dc314a83c60c120f8b906d4915f1` |
| PNGs Web/05bg_central_de_Ajuda.jpg | JPG | 55250 | `8e3bde42a51260222d6a66a1cc0bb705927430ac820c7afcd0d6b879f7d67f48` |
| PNGs Web/BG_breve.jpg | JPG | 72248 | `b1201d3880ad3e2231822920c8aa6cd24c0491994e7802a32ec341ae69182f3d` |
| PNGs Web/Logo_Central_De_Ajuda.png | PNG | 13606 | `add0c1d21363da3146e6c1fe8953a591be694762840e9cbe914e9236c4445ba9` |
| PNGs Web/Logo_Emails.png | PNG | 11437 | `4e23e5ab65fccb52167045cda6292015632fb27299216b8d889c29341a8eb36a` |
| PNGs Web/avatar_redessociais.png | PNG | 26243 | `f81a68900fe5db71d994b4ed5c968e5d1f4bb32c5bc3258b5962c8e30fdefdeb` |
| PNGs Web/bg_bco.jpg | JPG | 52233 | `43cd07d7a778671c0780d1aa53b7d1701c7ddd7c790b624b2ba2be4d75791968` |
| PNGs Web/bg_central_de_Ajuda.jpg | JPG | 109179 | `3a2dc778fd46aa4f2c8ce8e2a63211aafca16ad581d615a94761c62b94499c3a` |
| PNGs Web/logo_big.png | PNG | 13181 | `3901c8b637c19197475f98fe082cf18987df126c874071de4e884204099899ff` |
| PNGs Web/logo_big_white.png | PNG | 10648 | `d5f3ecd44c23eb27a9eb942d4fbb8247b83f215c934199cb6a90a064c1224b96` |
| PNGs Web/postlink.jpg | JPG | 91987 | `32e6c1772bb0cbe6bb1fb5507d43ccc7587132aff5739165e332edce672bc4a6` |
| avatar-110fbd83b3ce90f5edc285b2350005e2.png | PNG | 1304289 | `63abd7b86f0d90e22b1b78022ce750a3106707888b5238e416571ffc34e70639` |
| new_Splash3x.png | PNG | 331251 | `5eb4286b7bc9c1bb8e8383efcaf67cd805354f98d7e0184ed13a9153fcbdfbd4` |
| splash_login.png | PNG | 76497 | `f91cc027917bf6a8954468053f8a42b2e01100d916f5fc524d02b4378e7cbfc7` |

## Pendências de produto

Confirmar funcionalidades reais, permissões, stack do consumidor, termos comerciais, direitos de imagens e identidade de suporte antes de criar telas e campanhas finais. O sistema visual não resolve essas lacunas de evidência.
