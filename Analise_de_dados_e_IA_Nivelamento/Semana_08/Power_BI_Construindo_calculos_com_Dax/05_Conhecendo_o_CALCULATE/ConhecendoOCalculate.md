# Conhecendo o CALCULATE

<a id="topo"></a>

## Sumário
- [Conhecendo o CALCULATE](#conhecendo-o-calculate)
  - [Sumário](#sumário)
  - [1. Projeto da aula anterior](#1-projeto-da-aula-anterior)
  - [2. Vendas por vendedores](#2-vendas-por-vendedores)
  - [3. Para saber mais: criando a tabela calendário](#3-para-saber-mais-criando-a-tabela-calendário)
  - [4. Mudando o contexto de filtro](#4-mudando-o-contexto-de-filtro)
  - [5. Para saber mais: transição de contexto](#5-para-saber-mais-transição-de-contexto)
  - [6. Filtrando com CALCULATE](#6-filtrando-com-calculate)
  - [7. Para saber mais: funções de filtro](#7-para-saber-mais-funções-de-filtro)
  - [8. Mão na massa: criando uma matriz](#8-mão-na-massa-criando-uma-matriz)
  - [9. O que aprendemos?](#9-o-que-aprendemos)

## 1. Projeto da aula anterior

Caso prefira, você pode acessar o projeto da [aula](https://github.com/thierryLchaves/Santander-Imersao-Digital/blob/f22d04a155a7a2c82e5f6f401505397e1b941980/Analise_de_dados_e_IA_Nivelamento/Semana_08/Power_BI_Construindo_calculos_com_Dax/src/projeto-dax-livraria-inicial.pbix) no ponto em que paramos na aula anterior.  

[↑ Voltar ao topo](#topo)

---
## 2. Vendas por vendedores

Dando seguimento ao nosso projeto, a ideia será analisar as vendas realizadas com base em um vendedor especifico, para isso iremos realizar a confecção de mais uma página para visualizar essa informação criando mais um visual de tabela, com apresentações das categorias e as informações vendas, margem e margem em %, porém para o vendedor David Neves.  
Para isso iremos reaproveitas as medidas que criamos anteriormente para o tipo de produto, porém modificando o tipo pelo vendedor, ou seja iremos substituir onde na função `FILTER()`, passamos o `PRODUTOS[TIPO] ="Ebook"`, para `Vendedores[Nome] = "David Neves"`, com isso podemos criar nosso cartão de visualização com nossas medidas filtradas pelo vendedor:  
<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/tab_david.png" alt="Informações por vendedor" width="45%"/>
    </td>
</tr>
</table>

Novamente percebemos o mesmo padrão já mencionado, em nossa base de dados, que é o de quanto maior a quantidade de vendas menor é o percentual de margem de lucro sobre o produto. 
[↑ Voltar ao topo](#topo)

---
## 3. Para saber mais: criando a tabela calendário

[↑ Voltar ao topo](#topo)

---
## 4. Mudando o contexto de filtro

[↑ Voltar ao topo](#topo)

---
## 5. Para saber mais: transição de contexto

[↑ Voltar ao topo](#topo)

---
## 6. Filtrando com CALCULATE

[↑ Voltar ao topo](#topo)

---
## 7. Para saber mais: funções de filtro

[↑ Voltar ao topo](#topo)

---
## 8. Mão na massa: criando uma matriz

[↑ Voltar ao topo](#topo)

---
## 9. O que aprendemos?

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
__Titulo:__ Conhecendo o CALCULATE
__Autor:__ Thierry Lucas Chaves  
__Data de Criação:__ 19-06-2026  
__Data de Modificação:__ 19-06-2026  
__Versão:__ "1.0"