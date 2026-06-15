# Conectando os dados

<a id="topo"></a>

## Sumário
- [Conectando os dados](#conectando-os-dados)
  - [Sumário](#sumário)
  - [1. Apresentação](#1-apresentação)
  - [2. Para saber mais: conta gratuita indisponível](#2-para-saber-mais-conta-gratuita-indisponível)
  - [3. Preparando o ambiente: Power BI e base de dados](#3-preparando-o-ambiente-power-bi-e-base-de-dados)
  - [4. Para saber mais: Business Intelligence](#4-para-saber-mais-business-intelligence)
  - [5. Construindo o cartão com a média de pets](#5-construindo-o-cartão-com-a-média-de-pets)
  - [6. Alinhamento configuração Power BI](#6-alinhamento-configuração-power-bi)
  - [7. Ajustando a visualização](#7-ajustando-a-visualização)
  - [8. Importando as pastas e mesclando as tabelas](#8-importando-as-pastas-e-mesclando-as-tabelas)
  - [9. Tipo de dado correto](#9-tipo-de-dado-correto)
  - [10. Conectando com o Google planilhas](#10-conectando-com-o-google-planilhas)
  - [11. Renomeando tabelas](#11-renomeando-tabelas)
  - [12. Faça como eu fiz](#12-faça-como-eu-fiz)
  - [13. O que aprendemos?](#13-o-que-aprendemos)

## 1. Apresentação

Nesse curso teremos a mesma dinâmica vista anteriormente nos demais diretórios desse repositório, iremos aprender uma nova ferramenta com base em uma premissa de implementação prática. 
Durante o curso em questão veremos algumas coisas aqui listadas:  
- O que é o B.I
- Pro que utilizar o Power BI?
- Importar diferentes formatos
- Tratar os dados no Power Query
- Importar dos dados tratados
- Criar colunas e medidas
- Criar visuais 
- Estilização do DashBoard 

Ao final do curso teremos construído um  dashboard similar a imagem abaixo:  
<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: center;">
    <img src="imgs/ModeloDash.png" alt="Modelo Final de DashBoard" width="50%"/>
    </td>
</tr>
</table>

---
## 2. Para saber mais: conta gratuita indisponível

Durante a realização da formação de Power BI, você perceberá que alguns cursos utilizam o Power BI Serviço, a plataforma online onde é possível publicar relatórios e dashboard, além de compartilhar com outras pessoas.

No entanto, sabemos que muitos alunos e alunas estão enfrentando dificuldades para criar uma conta gratuita do Power BI. Isso está acontecendo porque, no momento, a Microsoft não está disponibilizando uma opção de criação de conta gratuita com tanta facilidade como antes, e o acesso ao Power BI Serviço está disponível apenas por meio de licenças pagas.

Apesar disso, não se preocupe, pois isso não afetará nos seus estudos. Você ainda poderá concluir todos os cursos da formação, mesmo sem acesso ao Power BI Serviço. A única diferença é que você não conseguirá publicar os relatórios online e importar alguns visuais, mas poderá fazer todo o projeto no Power BI Desktop, que é gratuito e fornece todas as funcionalidades necessárias durante a formação.

A Microsoft realiza atualizações com alta frequência, então isso pode mudar em breve. Se surgir uma nova maneira de criar uma conta gratuita, vamos comunicar a você. Por enquanto, você pode realizar os cursos da formação de Power BI sem empecilhos.

Em caso de dúvidas, entre em contato conosco pelo Discord da Alura ou pelo canal de atendimento ao estudante.

[↑ Voltar ao topo](#topo)

---
## 3. Preparando o ambiente: Power BI e base de dados
Neste curso, vamos aprender a construir um dashboard utilizando o [Power BI](https://www.microsoft.com/pt-br/power-platform/products/power-bi/). Para que possamos realizar as práticas do curso, precisamos instalar o Power BI Desktop e baixar os arquivos que serão utilizados.  
Abaixo, disponibilizo os materiais e passo a passo para fazermos isso.  

__Material do curso__
Durante o curso, iremos construir um dashboard utilizando uma base de dados contendo informações sobre um petshop. O material deste curso está disponível no [diretório de dados padrão do módulo](Analise_de_dados_e_IA_Nivelamento\Semana_07\Power_BI_Desktop_Construindo_meu_primeiro_dashboard\db).  

__Instalação do Power BI__  
- 1º Acesse a [página de download](https://www.microsoft.com/pt-br/power-platform/products/power-bi/downloads) do Power BI.
- 2º Na página de download, você encontrará diversas opções. Procure pela opção Microsoft Power BI Desktop e clique em Fazer download:
> <table style="text-align: center; width: 50%;"> 
> <tr>
> <td style="text-align: left;">
> <img src="imgs/msg_download.png" alt="Msg_donwload" width="45%"/>
> </td>
> </tr>
> </table>
- 3º Após essa ação, você será redirecionado para uma página em branco, onde será solicitada a abertura da loja da Microsoft. Clique em Abrir Microsoft Store:
> <table style="text-align: center; width: 100%;"> 
> <tr>
> <td style="text-align: left;">
> <img src="imgs/MSTORE.png" alt="Microsoft Store" width="45%"/>
> </td>
> </tr>
> </table>
- 4º Com a página inicial do Power BI Desktop na loja da Microsoft aberta, você pode clicar em Instalar:
> <table style="text-align: center; width: 70%;"> 
> <tr>
> <td style="text-align: left;">
> <img src="imgs/Instal_pbi.png" alt="InstalL Power Bi" width="45%"/>
> </td>
> </tr>
> </table>
- 5º Nessa etapa, é necessário aguardar a instalação ser finalizada. Após a instalação ser concluída, você pode clicar em Abrir:
> <table style="text-align: center; width: 70%;"> 
> <tr>
> <td style="text-align: left;">
> <img src="imgs/finished_install_pbi.png" alt="Final InstalL Power Bi" width="45%"/>
> </td>
> </tr>
> </table>
- 6º Pronto! Finalizamos a instalação do Power BI Desktop. Agora você já pode utilizá-lo e dar sequência às atividades do curso.

[↑ Voltar ao topo](#topo)

---
## 4. Para saber mais: Business Intelligence  
Nos contrataram para participar de um projeto para o petshop Gatito, da Helô. Seu desejo é atualizar seu negócio para crescer e abrir novas filiais.  

Helô descobriu que, para isso, é importante incorporar o BI em sua empresa. Esse será o nosso papel no projeto.  

Mas, o que significa o termo "BI"? É o mesmo que Power BI? Para começar, vamos entender esse conceito.   

B.I. é uma sigla para o termo "Business Intelligence", do inglês. Podemos traduzi-lo como "Inteligência de Negócios". Que empresa não quer ser inteligente?!  

Mas, o que está por trás desse conceito de inteligência de negócios? Uma pessoa executiva super genial que consegue elaborar tomadas estratégicas de decisão?  

Na verdade, não. O conceito de BI é relacionado ao trabalho estruturado com os dados da empresa, trazendo métricas para que as pessoas tomadoras de decisão da empresa possam dar os direcionamentos necessários para o negócio baseados em dados.  

Esse conceito não é novo e surgiu na década de 1960. Mas, claro, nessa época a tecnologia ainda era muito embrionária. Então, o Business Intelligence ainda era bastante relacionado às decisões estratégicas.  

Na realidade atual, tudo ao nosso redor gera dados. Isso é extremamente importante e valioso para as empresas pois, com dados, elas podem definir métricas para entender exatamente o que está acontecendo com o negócio.  

Assim, elas podem traçar previsões não baseadas em achismos, mas em fatos. Isso é fundamental para alavancar a empresa para outros patamares.  

É importante salientar que a implementação do BI numa empresa não termina na estruturação de dados e definição de métricas. Muitas vezes, a pessoa que recebe as nossas análises não é uma pessoa técnica da área.  

Dessa forma, é essencial conseguir organizar todas as nossas análises e caminhos tomados. Para isso, utilizamos a técnica de Storytelling, que podemos traduzir como "contação de história" — a história das nossas análises.  

Nós apresentamos essa história de uma forma facilmente consultável pelas pessoas que precisam dessas informações. É por isso que construímos Dashboards, que podemos traduzir como "painel".  

Nesse painel, inserimos uma série de gráficos e elementos visuais que ajudam a pessoa a compreender rapidamente o que está acontecendo com a empresa, baseando-se nessas informações para tomar decisões.

Além disso, o dashboard pode ser atualizado em tempo real, possibilitando acompanhamento e análise constantes sobre o estado de diferentes setores da empresa.  

[↑ Voltar ao topo](#topo)

---
## 5. Construindo o cartão com a média de pets
O primeiro passo para confecção assertiva de nosso primeiro DashBoard, será importar os dados para dentro do Power B.I, para isso iremos selecionar na tela inicial do relatório em branco sobre a guia de `página inicial`, a opção de __obter dados__, assim como em outras ferramentas vide exemplo no processo de importação de dados para o Excel, o Power B.I também nos possibilita a obtenção de dados externos, quando clicamos diretamente sobre o botão de obter dados seremos apresentados a tela  com informações de importação de dados das principais fontes possíveis de utilização: 
<table style="text-align: center; width: 70%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/Obtencao_dados.png" alt="Obter dados Power BI" width="45%"/>
    </td>
</tr>
</table>

A tela da imagem acima, nos mostra todas as possibilidades de conexão possíveis de serem realizadas com  o Power B.I, porém para o nosso casso em questão iremos acessar o [arquivo de clientes]() disponível em nosso repositório que está em formato `CSV`, portanto a fonte de conexão escolhida 



[↑ Voltar ao topo](#topo)

---
## 6. Alinhamento configuração Power BI

[↑ Voltar ao topo](#topo)

---
## 7. Ajustando a visualização

[↑ Voltar ao topo](#topo)

---
## 8. Importando as pastas e mesclando as tabelas

[↑ Voltar ao topo](#topo)

---
## 9. Tipo de dado correto

[↑ Voltar ao topo](#topo)

---
## 10. Conectando com o Google planilhas

[↑ Voltar ao topo](#topo)

---
## 11. Renomeando tabelas

[↑ Voltar ao topo](#topo)

---
## 12. Faça como eu fiz

[↑ Voltar ao topo](#topo)

---
## 13. O que aprendemos?

[↑ Voltar ao topo](#topo)

---

<!-- <table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/ex.png" alt="Nome do print" width="45%"/>
    </td>
</tr>
</table> -->

---

<table align="center" style="border-collapse: collapse; margin-left: auto; margin-right: auto;"> 
  <caption><b>Skills do projeto</b></caption>
  <tr>
    <td style="padding: 5px;">
      <img alt="VS Code" src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>
    </td>
    <td style="padding: 5px;">
      <img alt="Markdown" src="https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white"/>
    </td>
    <td style="padding: 5px;">
      <img alt="Power BI" src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black"/>
    </td>
  </tr>
</table>


---
__Titulo:__ Conectando os dados
__Autor:__ Thierry Lucas Chaves  
__Data de Criação:__ 14-06-2026  
__Data de Modificação:__ 14-06-2026  
__Versão:__ "1.0"