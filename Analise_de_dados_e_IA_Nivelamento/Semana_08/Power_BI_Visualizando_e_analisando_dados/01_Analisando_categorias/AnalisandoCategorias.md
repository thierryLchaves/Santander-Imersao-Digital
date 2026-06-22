# Analisando categorias

<a id="topo"></a>

## Sumário
- [Analisando categorias](#analisando-categorias)
  - [Sumário](#sumário)
  - [1. Apresentação](#1-apresentação)
  - [2. Para saber mais: conta gratuita indisponível](#2-para-saber-mais-conta-gratuita-indisponível)
  - [3. Preparando o ambiente](#3-preparando-o-ambiente)
  - [4. Explorando os dados](#4-explorando-os-dados)
  - [5. Identificando a melhor forma de visualização](#5-identificando-a-melhor-forma-de-visualização)
  - [6. Refletindo sobre o gráfico de pizza](#6-refletindo-sobre-o-gráfico-de-pizza)
  - [7. Para saber mais: usos do gráfico de pizza](#7-para-saber-mais-usos-do-gráfico-de-pizza)
  - [8. Análise com gráfico de pizza](#8-análise-com-gráfico-de-pizza)
  - [9. Faça como eu fiz: crie uma hierarquia](#9-faça-como-eu-fiz-crie-uma-hierarquia)
  - [10. O que aprendemos?](#10-o-que-aprendemos)

## 1. Apresentação

Assim como em todos os outros cursos desse repositório, esse curso irá ter como premissa um projeto, porém desse curso em questão iremos trabalhar em um projeto que estaremos sob a égide de um loja de cosméticos, porém as informações dessa loja __NÃO É ORIENTADA A DADOS__, porém o objetivo e realizar uma maneira que possamos incluir essa empresa para a <a href="#CULTdd"> Cultura Data-Driven </a>, então sobre nosso objetivo para além de atender a essa demanda, iremos entender quais são os melhores gráficos a serem aplicados para cada tipo de análise a serem feitas. 

Ao finalizar esse projeto, teremos como resultado um DashBoard similar ao da imagem abaixo:  
<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/rel_final.png" alt="Relatório final" width="45%"/>
    </td>
</tr>
</table>

<details id="CULTdd">
    <summary> Cultura Data-Driven</summary>
    <p>É um modelo de gestão em que as decisões estratégicas, operacionais e de negócios são baseadas na análise e interpretação de dados, em vez de intuição, palpites ou experiências puramente subjetivas.</p>
    <ul>
        <li><strong>Democratização dos Dados:</strong> Garante que os dados não fiquem restritos apenas à equipe de TI ou cientistas de dados, permitindo que diferentes setores tenham autonomia para acessar e analisar informações relevantes.</li>
        <li><strong>Mentalidade Analítica:</strong> Estimula um ambiente focado em testes, experimentações e validação de hipóteses, onde os erros são identificados rapidamente por meio de métricas claras e transformados em aprendizado.</li>
        <li><strong>Foco em Resultados Reais:</strong> Substitui o viés de autoridade (a opinião de quem tem o cargo mais alto) por fatos concretos, otimizando processos, reduzindo custos e aumentando a previsibilidade do negócio.</li>
    </ul>
</details>

[↑ Voltar ao topo](#topo)

---
## 2. Para saber mais: conta gratuita indisponível  

Durante a realização da formação de Power BI, você perceberá que alguns cursos utilizam o Power BI Serviço, a plataforma online onde é possível publicar relatórios e dashboard, além de compartilhar com outras pessoas.

No entanto, sabemos que muitos alunos e alunas estão enfrentando dificuldades para criar uma conta gratuita do Power BI. Isso está acontecendo porque, no momento, a Microsoft não está disponibilizando uma opção de criação de conta gratuita com tanta facilidade como antes, e o acesso ao Power BI Serviço está disponível apenas por meio de licenças pagas.

Apesar disso, não se preocupe, pois isso não afetará em nada nos seus estudos. Você ainda poderá concluir todos os cursos da formação, mesmo sem acesso ao Power BI Serviço. A única diferença é que você não conseguirá publicar os relatórios online, mas poderá fazer todo o projeto no Power BI Desktop, que é gratuito e fornece todas as funcionalidades necessárias durante a formação.

A Microsoft realiza atualizações com alta frequência, então isso pode mudar em breve. Se surgir uma nova maneira de criar uma conta gratuita, vamos comunicar a você. Por enquanto, você pode realizar os cursos da formação de Power BI sem empecilhos.

Em caso de dúvidas, entre em contato conosco pelo Discord da Alura ou pelo canal de atendimento ao estudante.

[↑ Voltar ao topo](#topo)

---
## 3. Preparando o ambiente  

Neste curso, vamos aprender a utilizar um projeto com os dados carregados no Power BI.

__Antes de começar…__  
<<<<<<< HEAD
Vamos acessar o [arquivo PBIX](https://github.com/thierryLchaves/Santander-Imersao-Digital/blob/0e2ab5e5e0eea0262620592fd010e7924433fd22/Analise_de_dados_e_IA_Nivelamento/Semana_08/Power_BI_Visualizando_e_analisando_dados/src/preparando_ambiente_analisando_visualizando_dados.pbix) que será utilizado durante o curso.

Além disso, vamos utilizar duas imagens que será usadas quando formos fazer a estilização do nosso relatório. Você também pode baixá-las [aqui](https://github.com/thierryLchaves/Santander-Imersao-Digital/blob/0e2ab5e5e0eea0262620592fd010e7924433fd22/Analise_de_dados_e_IA_Nivelamento/Semana_08/Power_BI_Visualizando_e_analisando_dados/src/Styles)

Por fim, caso você queira explorar e ir além no seu projeto, pode ficar à vontade para [acessar a base de dados do projeto](https://github.com/thierryLchaves/Santander-Imersao-Digital/blob/0e2ab5e5e0eea0262620592fd010e7924433fd22/Analise_de_dados_e_IA_Nivelamento/Semana_08/Power_BI_Visualizando_e_analisando_dados/db/Base_de_dados-Opuline.xlsx) e realizar suas próprias transformações e análises.

[↑ Voltar ao topo](#topo)

---
## 4. Explorando os dados

A ideia com esse projeto e que possamos analisar os dados disponibilizados pela empresa, para que possamos auxilia-los sobre o seu comércio, iremos identificar padrões, tendências, realizar previsões, e outras coisas...  
Porém como temos o foque em outras utilizações, dentro do Power B.I não iremos realizar os processos de extração e carregamento e tratamento dos dados, e por tal motivo iniciaremos nosso projeto com o [arquivo](https://github.com/thierryLchaves/Santander-Imersao-Digital/blob/0e2ab5e5e0eea0262620592fd010e7924433fd22/Analise_de_dados_e_IA_Nivelamento/Semana_08/Power_BI_Visualizando_e_analisando_dados/src/preparando_ambiente_analisando_visualizando_dados.pbix) já iniciado.    

> PS: Adendo em nosso projeto, foi realizado a criação de parâmetro para fonte de dados, para que não ocorra erros

--- 
Então para iniciarmos o nosso projeto vamos, com a realizar algumas provocações .  _Qual será o melhor visual para trabalhar com um séria temporal ?, ou ainda qual seria  o melhor visual para comprar categorias ?_

Mas antes de iniciarmos qualquer trabalho é importante que tenhamos ciência de como está divdida nossa base de dados, para isso iremos acessar a guia de modelagem e visualizar nossa base

<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/Modelagem_Dados.png" alt="Modelo de relacionamento" width="45%"/>
    </td>
</tr>
</table>

A partir de visualizarmos, quais são as tabelas, e como elas selecionam, iremos partir para construção do primeiro gráfico no projeto, e para construção de qualquer informação precisamos de um contexto e esse contexto é a necessidade de entender como está o faturamento pelas categorias, e antes de criar propriamente dito esse novo visual vamos explorar as informações com uma tabela.
Quando realizamos a inserção do card de tabela e selecionarmos as informações de categoria _(está presente na base com formato hierárquico)_, assim como suas subcategorias, e por fim adicionarmos a medida de faturamento, termo um visual conforme abaixo:  

<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/Analise_tabular_primaria.png" alt="Analise primária em tabela" width="45%"/>
    </td>
</tr>
</table>

Porém podemos modificar essa visualização modificando o layout desse card, para o modelo de matriz, com essa visualização teremos um visualização ainda mais concisa da informação, porém com visual menos agressivo:

<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/visualizacao_matriz.png" alt="Analise matriz " width="45%"/>
    </td>
</tr>
</table>

As informações estão agregadas por categorias e expandidas em suas subcategorias, com esse modelo de visualização já conseguimos responder nosso questionamento e visualizamos qual é qual é categoria com maior faturamento na loja, e se organizamos os dados pelo faturamento visualizamos que a categoria com maior rentabilidade é a de maquiagem.  
Porém será que de fato essas visualizações são as melhores ou mais indicadas para esse tipo de visualização ? ou podemos ter outras melhores. 


[↑ Voltar ao topo](#topo)

---
## 5. Identificando a melhor forma de visualização   

Para começar a acompanhar as vendas da Opuline, você precisa escolher a melhor forma de visualizar os dados de vendas de modo a proporcionar clareza e facilidade de análise para a equipe, que está se familiarizando com a análise de dados. Considerando que a empresa tem produtos divididos em várias categorias e subcategorias, qual é a melhor visualização inicial para explorar o faturamento por categoria e subcategoria?  

<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/Prova_Questoes/RESP_1.png" alt="Resposta Melhor  visualização " width="45%"/>
    </td>
</tr>
</table>



[↑ Voltar ao topo](#topo)

---
## 6. Refletindo sobre o gráfico de pizza

[↑ Voltar ao topo](#topo)

---
## 7. Para saber mais: usos do gráfico de pizza

[↑ Voltar ao topo](#topo)

---
## 8. Análise com gráfico de pizza

[↑ Voltar ao topo](#topo)

---
## 9. Faça como eu fiz: crie uma hierarquia

[↑ Voltar ao topo](#topo)

---
## 10. O que aprendemos?

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
__Titulo:__ Analisando categorias
__Autor:__ Thierry Lucas Chaves  
__Data de Criação:__ 19-06-2026  
__Data de Modificação:__ 19-06-2026  
__Versão:__ "1.0"