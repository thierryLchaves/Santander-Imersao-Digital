# Formulas e Funções

# Sumário 
---
## 1. Preparando o ambiente: planilha Meteora E-commerce
Para acompanhar o curso com o máximo de aproveitamento, você pode fazer o download da [planilha](src/Meteora%20Ecommerce%20-%20FINAL%20AULA%202.xlsx) que estamos trabalhando para a Loja Meteora

## 2. Aplicando cálculos
O desafio primário proposto, é realizar a confecção de uma linha de totais.
> PS: Atualmente nossa pasta de trabalho consta com duas planilhas, uma __com__ e outra __sem__ formatação de tabela.  

Nesta aula iremos realizar tal processo na planilha __sem__ a tabela, devido ao retrabalho de edição em duas planilhas. 
Para realizar o processo, primeiro iremos realizar a `auto-soma` disponibilizada pelo Excel, essa opção que está disponível na guia de Página Inicial, e uma maneira um pouco restritiva, pois ela é possível de ser feita com número médias etc.., como o próprio nome diz ela realiza a soma de números. 
Outra maneira de realizar essa somatória e através de formulas, uma maneira de realizar essa formula segue o modelo abaixo:

```Excel
=D1+D2+D3+D4
```
Outra maneira de realizar esse processo, e esse é o mais recomendado se da na utilização de __funções__, para que uma função no Excel, seja utilizada segue-se uma premissa básica na célula que recebera aquela função, essa seguindo a notação de:  
```Excel
=soma(parâmetros)
```
os parâmetros que serão inseridos na função, no caso da função soma é o intervalo de valores que se deseja inserir, esse intervalo e demonstrado a __primeira célula : ultima célula__
<table style="text-align: center; width: 50%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/funcao_soma.png" alt="Função de soma de intervalos" width="30%"/>
    </td>
</tr>
</table>

> Quando for necessário realizar a soma de células especificas, substitui-se o caractere de `:` para o de `;`, dessa maneira o Excel, irá realizar a somente os valores das células e não do intervalo em sí.

Outro ponto importante sobre a utilização de funções é que o valor da célula e ajustado conforme os valores do intervalo mudam, ou seja a somatória das células selecionadas ocorrem de forma dinâmica, e nesse cenário sobre utilização de funções existem duas maneiras de identificar a utilização de uma, sendo elas abrindo a célula para verificar o valor inserido, ou selecionado a célula desejada, e verificando o seu valor dentro da barra de formulas.

---
Já para realizar o processo de soma dentro de uma planilha com formatação de tabela, existe uma maneira mais rápida para essa funcionalidade, através da guia de __Design da Tabela__, existe a opção de linha de totais, que somente é apresentada em espaços com formatação de tabela, nessa guia é possível realizar a seleção da Flag de __Linha de totais__, com essa opção marcada, será realizado a totalização de forma automática. 
<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/Design_Tabela.png" alt="Design de tabela linha de totais" width="100%"/>
    </td>
</tr>
<tr>
    <td style="text-align: left;">
    <img src="imgs/total_criado.png" alt="Resultado de totalização de linhas" width="50%"/>
    </td>
</tr>
</table>
Dessa maneira para além de já realizar a soma de um campo a formatação em tabela também oferece a opção de inserção de outras funções nas linhas escolhidas,como por exemplo a função de soma na coluna dos valores
<table style="text-align: center; width: 60%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/opc_linha_totais.png" alt="Opções de funções formatação de tabela" width="50%"/>
    </td>
</tr>
</table>

## 3. Calculando o total de vendas
<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/Prova_Questoes/Calculando_total.png" alt="Calculando o total de vendas" width="100%"/>
    </td>
</tr>
</table>

## 4. Tipos de referências
Ao longo do curso foi afirmado reiteradas vezes, que a utilização de formatação de tabela devia ser utilizada com tabela, e um dos motivos para tal cautela se deve ao fato das referências, quando estamos utilizando formulas em planilhas não formatadas, as referências as células utilizada são <a href="#ref_relativa">referências relativas</a>, porém quando estamos trabalhando com tabelas, o Excel realiza <a href="#ref_estruturada">referências estruturadas </a>, de forma simples a explicação dessas referências pode ser entendida da seguinte maneira, em referência relativas: o Excel utiliza o intervalo selecionado como sua referência por exemplo `=soma(__D4:D23__)`, dessa maneira a referência do intervalo selecionado para aplicação fa função está referenciando diretamente o intervalo daquela planilha, porém quando estamos falando de referências estruturadas: o Excel irá realizar os nomes das tabelas para fazer as somas por exemplo `=SUBTOTAL(__109;[Preço Unitário]__)`, diferente da planilha sem estrutura de tabela o Excel, selecionou a função __SUBTOTAL__, que recebe 2 parâmetros como input, sendo eles, o número da função a ser utilizada _(no caso 109)_, e o nome da coluna da tabela que está entre colchetes, com o nome da coluna isso fica explicito quando por exemplo selecionamos uma determinada célula de uma coluna o valor anteriormente escrito com o nome da célula muda para o nome da coluna, o que pode ser entendido como o Excel identificando o nome do cabeçalho sendo como o nome da coluna.
Ao realizar referências relativas, em planilhas não tabulares, pode ser realizado por exemplo o atalho de copiar e colar(ou de arraste do valor da célula) das formulas uma vez que as referências são feitas com base na posição das linhas com as colunas, o Excel realiza automaticamente a mudança do intervalo para a coluna desejada.
>PS: Ainda exite a __Referência Absoluta__, e para sua utilização sobre o valor desejado pode utilizar a tecla `F4`, fica demarcado com o caractere de `_$_`, sobre os valores.

<details id="ref_relativa">
<summary>Referência Relativa </summary>
    <p> É o método de referência padrão do Excel. Uma referência relativa (ex: A1) indica o endereço de uma célula em relação à posição da célula que contém a fórmula. </p>
    <ul>
        <li> <b>Comportamento:</b> Ao copiar ou arrastar uma fórmula com referência relativa para outras células, o Excel ajusta automaticamente o endereço com base no deslocamento de linhas e colunas. </li>
        <li> <b>Aplicação:</b>  Ideal para cálculos simples onde a mesma operação é aplicada em uma sequência de células adjacentes.</li>
        <li> <b>Exemplo:</b> Se a fórmula na célula C1 for =A1*B1, ao arrastá-la para C2, o Excel a ajustará automaticamente para =A2*B2.</li>
    </ul>
</details>

<details id="ref_estruturada">
    <summary>Referência Estruturada </summary>
        <p>
        Introduzida para trabalhar especificamente com Tabelas do Excel (funcionalidade Insert > Table ou Ctrl+T). Em vez de usar endereços de células (ex: A1), utiliza-se o nome da tabela e dos cabeçalhos das colunas (ex: Tabela1[Valor]).
        <ul>
            <li> <b>Comportamento:</b> É intrinsecamente "absoluta" em relação à coluna. Ao adicionar novos dados à tabela, a fórmula se expande automaticamente (propagação).</li>
            <li><b>Vantagens:</b> Alta legibilidade (o usuário entende o contexto da conta, como "Preço * Quantidade" em vez de "A2 * B2") e robustez (a fórmula não quebra se colunas forem inseridas ou deletadas).</li>
            <li><b> Sintaxe comum:</b> [@Coluna]: Referência ao item na mesma linha. Tabela1 [Coluna]: Referência à coluna inteira. </li>
        </ul>
</details>


## 5. Calculando o valor do desconto
## 6. Faça como fiz: Linha de totais
## 7. O que aprendemos ?

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
      <img alt="Excel" src="https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white"/>
    </td>
  </tr>
</table>

---
__Titulo:__ Formulas e Funções  
__Autor:__ Thierry Lucas Chaves  
__Data de Criação:__ 01-05-2026  
__Data de Modificação:__ 01-05-2026  
__Versão:__ "1.0"