<a id="topo"></a>

# Estruturando o dashboard

## Sumário
- [Estruturando o dashboard](#estruturando-o-dashboard)
  - [Sumário](#sumário)
  - [1. Projeto da aula anterior](#1-projeto-da-aula-anterior)
  - [2. Estruturando o painel](#2-estruturando-o-painel)
  - [3. Criando indicadores](#3-criando-indicadores)
  - [4. Somando com uma condição](#4-somando-com-uma-condição)
  - [5. Preparando os dados](#5-preparando-os-dados)
  - [6. Faça como eu fiz: calculando os indicadores](#6-faça-como-eu-fiz-calculando-os-indicadores)
  - [7. O que aprendemos?](#7-o-que-aprendemos)

---

## 1. Projeto da aula anterior

Continuando a nossa jornada neste curso você pode acessar [aqui](db/Meteora%20Ecommerce%20-%20FINAL%20AULA%201.xlsx) o projeto da aula anterior

## 2. Estruturando o painel
> PS O curso não se destina sobre utilização ou criação de DashBoards, porém serão visto comandos e normas de como realizar a construção de gráficos. 

Para a construção do DashBoard/Gráfico iremos criar uma nova planilha para tal, é de suma importância que para a construção desses gráficos não seja misturados tais dados em uma mesma planilha.
Uma das dicas passadas no curso diz respeito a formatação de Altura e largura das `colunas/linhas`, para o seguimento do processo realizamos a formatação de toda a planilha com os valores 
```text
height: +- 9 px
width: +- 1,30 px
```
Com esse processo de ajuste total da planilha nos auxilia, tanto na divisão de colunas que serão inseridas para confecção dos painéis. Para ajuste da planilha iremos realizar a seleção de __18__ colunas  e 6 linhas a partir da `Coluna C`, e posteriormente deixaremos mais 2 colunas vagas após essa seleção e repetiremos o intervalo, fazendo esse processo teremos um resultado similar a esse:
<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/modelo_selecao_planilha.png" alt="Desenho planilha" width="45%"/>
    </td>
</tr>
</table>

> PS: Uma sugestão dada durante a aula, foi de que ao serem criados DashBoards os primeiros Painéis sejam aquelas que contenham as informações mais relevantes.

## 3. Criando indicadores

Feito as configurações sugeridas no módulo anterior daremos seguimento a outras formatações, uma delas sendo a opção de _`Recolher Faixa de opções`_ esse recurso de mouse pode ser realizado em qualquer uma das guias do Excel.
Para além disso para melhor apresentação dessa planilha, podemos ocultar as linhas de grade, dentro da guia _Exibir_ desmarca a opção de linhas de grade, fazendo assim com que nosso Dashboard fique da seguinte forma:

<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/desenho_dash_board_2.png" alt="Desenho planilha 2" width="45%"/>
    </td>
</tr>
</table>

Apenas para relembramos algumas formulas que já vimos anteriormente, para a tabela de produtos utilizaremos a formula de contagem de valores, e para essa contagem a formula utilizada é a de 
```exel
=CONT.VALORES(Produtos!B4:B42)
```
Essa formulá pode ser feita tanto dessa maneira quanto da maneira abaixo:
```excel
=CONT.VALORES(TB_Produtos[Código])
```
Na formulá acima utiliza-se do processo de referência estruturada, e essa pode ser mais segura dado que caso sejam acrecidos valores na tabela ou modificados esse valor será atualizado , utilizaremos o processo de referência estruturada também para os demais cards, com as formulas abaixo:
```excel
=SOMA(TB_Vendas[Qtd])

=SOMA(TB_Vendas[Total])
```
<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/Prova_Questoes/TB_VERDADE.png" alt="TAB VERDADE" width="45%"/>
    </td>
</tr>
</table>

Camila, a gerente da empresa deseja contar quantas respostas válidas foram dadas por cada funcionário no total. Mas está na dúvida de qual função ela deve utilizar.

Baseado no que aprendemos na aula, vamos ajudar a Camila a escolher a função correta para calcular a quantidade de respostas válidas?
<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/Prova_Questoes/RESP_TAB_VERDADE.png" alt="RESPOSTA TABELA VERDADE" width="45%"/>
    </td>
</tr>
</table>

## 4. Somando com uma condição
Em uma pesquisa de satisfação em uma empresa, os funcionários responderam a algumas perguntas usando Verdadeiro ou Falso.


## 5. Preparando os dados

## 6. Faça como eu fiz: calculando os indicadores

## 7. O que aprendemos?

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
  </tr>
</table>


---
__Titulo:__ Estruturando o dashboard
__Autor:__ Thierry Lucas Chaves  
__Data de Criação:__ 17-05-2026  
__Data de Modificação:__ 17-05-2026  
__Versão:__ "1.0"