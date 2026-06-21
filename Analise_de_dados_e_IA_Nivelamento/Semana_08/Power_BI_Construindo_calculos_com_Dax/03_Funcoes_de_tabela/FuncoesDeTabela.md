# Funções de tabela

<a id="topo"></a>

## Sumário
- [Funções de tabela](#funções-de-tabela)
  - [Sumário](#sumário)
  - [1. Projeto da aula anterior](#1-projeto-da-aula-anterior)
  - [2. Vendas por categoria](#2-vendas-por-categoria)
  - [3. Vendas por tipo de produto](#3-vendas-por-tipo-de-produto)
  - [4. Para saber mais: função FILTER](#4-para-saber-mais-função-filter)
  - [5. Destacando métricas](#5-destacando-métricas)
  - [6. Para saber mais: RELATED e RELATEDTABLE](#6-para-saber-mais-related-e-relatedtable)
  - [7. Filtrando regiões](#7-filtrando-regiões)
  - [8. Mão na massa: calculando vendas com filtros](#8-mão-na-massa-calculando-vendas-com-filtros)
  - [9. O que aprendemos?](#9-o-que-aprendemos)

## 1. Projeto da aula anterior 
Caso prefira, você pode acessar o projeto da [aula](https://github.com/thierryLchaves/Santander-Imersao-Digital/blob/f22d04a155a7a2c82e5f6f401505397e1b941980/Analise_de_dados_e_IA_Nivelamento/Semana_08/Power_BI_Construindo_calculos_com_Dax/src/projeto-dax-livraria-inicial.pbix) no ponto em que paramos na aula anterior.  

[↑ Voltar ao topo](#topo)

---
## 2. Vendas por categoria
Até o presente momento nosso projeto está estruturado de forma que temos uma visão individual de cada produto de uma maneira mais analítica sobre as vendas e sua margem de lucro, porém seria interessante obtermos uma visão agrupada sobre as categorias de cada produto, ou seja o que iremos realizar agora é uma maneira de obtermos uma visão mais agregada sobre os produtos. 
Para esse processo iremos criar uma nova página para essa visualização iremos criar um novo CARD de tabela, porém agora os campos que selecionaremos para apresentação dessa tabela será a categoria dos livros presentes na tabela de produtos, e as medidas que foram criadas anteriormente. com isso teremos um resultado conforme do exemplo abaixo:  
<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/vendas_por_categoria.png" alt="Tabela de vendas por categoria" width="45%"/>
    </td>
</tr>
</table>

Ao analisar esse quadro temos uma nova visão sobre nossa vendas, se reparamos no card percebemos que por exemplo a categoria de __Data Science__ apesar de possuir o maior montante de vendas, é que possui a menor margem de lucro, e assim segue as categoria de __SQL e Big Data__, possuem uma margem inferior ao sua quantidade de vendas ficando abaixo dos 40% enm relação ao valor total das vendas. 
A frente iremos especificar ainda mais nossa visão obtendo a subdivisão das categoria pelos tipos de produtos, e isso é o que faremos no [tópico seguinte](#3-vendas-por-tipo-de-produto). 

[↑ Voltar ao topo](#topo)

---
## 3. Vendas por tipo de produto
Para que possamos realizar uma nova visualização focada pelo tipo de produto, nos iremos realizar uma nova fórmula utilizando `DAX`, para podermos utilizar nossas medidas com base no tipo do produto. 
Para isso iremos criar uma nova medida para realizar a soma do total de produtos com base em um filtro, nossa fórmula para isso será a seguinte:  
```DAX
Vendas Ebook = 
SUMX(
    FILTER( 
        Vendas,
        RELATED(Produtos[Tipo]) = "Ebook"
    ),
    Vendas[Quantidade] * Vendas[Preco Calculado]
) 
```
A forma acima, realizada uma soma de forma iterada, porém com base em um valor de filtro por isso utilizamos a função `FILTER`, essa função exige 2 parâmetros no caso a base na qual será aplicado o filtro, e o segundo qual é o filtro a ser aplicado, porém como nosso mote inicial é realizar um filtro com base no tipo do livro que está presente somente na tabela de produtos, realizamos então a utilização da função `RELATED` que é uma função que realiza o relacionamento de forma tabular entre duas tabelas, então com essa função conseguimos comparar nossa tabela de produtos no campo tipo igual a nossa condição que seria _Ebook_, aplicada diretamente a nossa tabela de vendas, com isso podemos utilizar essa expressão como a tabela do primeiro parâmetro exigido pela função `SUMX()`, e aplicar o restante da formula.  
Com essa nova medida, podemos visualizar diretamente em tela comparando a diferença entre a vendas total e as vendas pelo tipo de produto Ebook:  
<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/Total_x_Ebook.png" alt="Total de vendas X Vendas por Tipo Ebook" width="45%"/>
    </td>
</tr>
</table>

Com isso iremos replicar a mesma lógica vistar anteriormente para as demais medidas, deixando as medidas da seguinte maneira:  
```DAX
Margem Ebook = 
SUMX(
    FILTER(
        Vendas,    
        RELATED(Produtos[Tipo]) = "Ebook"
        ),
    Vendas[Quantidade] * (Vendas[Preco Calculado] - Vendas[Custo Calculado])
)

Margem Ebook % = DIVIDE([Margem Ebook],[Vendas Ebook],0)
```
Quando aplicarmos essa fórmulas criadas acima, teremos uma visualização sobre o cenário de vendas quando o produto é do tipo _Ebook_, conforme imagem abaixo:  
<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/Vendas_por_Ebook.png" alt="Total de vendas pelo tipo de Ebook" width="45%"/>
    </td>
</tr>
</table>

Na segunda tabela visualizamos que a proporção de vendas ainda não acompanha a margem de lucro sobre o produto isso pode ser notado pela categoria de SQL, na qual temos o maior valor de vendas, porém com a menor margem. Porém ainda conseguimos melhorar a visão sobre as vendas, e seria interessante trazer de forma destacada sem que sejam responsivos ao clique das tabelas, deixando um cartão com valores fixo para o tipo de produto _Ebook_.  


[↑ Voltar ao topo](#topo)

---
## 4. Para saber mais: função FILTER
A função `FILTER` é uma das funções mais poderosas e versáteis no DAX (Data Analysis Expressions). Essa função permite criar tabelas filtradas com base em condições específicas, oferecendo uma maneira flexível de manipular e analisar dados.

---

__Funcionamento da Função FILTER__  
A função FILTER opera iterando sobre uma tabela e avaliando uma expressão booleana (uma condição) para cada linha dessa tabela. As linhas que atendem à condição especificada são incluídas na tabela resultante, enquanto as linhas que não atendem à condição são ignoradas. A sintaxe básica da função FILTER é a seguinte:
```DAX
FILTER(tabela, condição)
```
Onde tabela é a __tabela__ que você deseja filtrar e condição é a expressão booleana que determina quais linhas serão incluídas na tabela resultante.  

__Retorno de uma Tabela__  

Ao contrário de muitas funções DAX que retornam um valor escalar, a função FILTER retorna uma tabela. Essa tabela contém todas as linhas da tabela original que atendem à condição especificada. Essa funcionalidade é especialmente útil quando você deseja usar o resultado da FILTER como entrada para outras funções DAX que operam em tabelas, como `CALCULATE, SUMX, AVERAGEX`, entre outras.

---
__Função Iteradora__  

Uma característica essencial da função FILTER é que ela é uma função iteradora. Isso significa que a FILTER avalia a condição especificada para cada linha individualmente na tabela de entrada. Como uma função iteradora, FILTER pode lidar com condições complexas que dependem de valores específicos de cada linha, permitindo uma análise detalhada e personalizada dos dados.

__Contexto de Linha__  
O conceito de contexto de linha é crucial para entender como a função FILTER e outras funções DAX funcionam. O contexto de linha refere-se ao ambiente no qual uma fórmula DAX é avaliada, especificamente, quais linhas e colunas estão disponíveis para a fórmula no momento da avaliação.  

No caso da função FILTER, a condição é avaliada para cada linha no contexto de linha dessa linha específica. Isso permite que a função FILTER crie filtros dinâmicos de acordo com o contexto.

Vamos explorar o conceito de contexto de linha com mais profundidade na aula 4.

__Exemplo de uso da Função FILTER__  

Vamos considerar um exemplo prático para ilustrar o uso da função FILTER. Suponha que você tenha uma tabela de vendas chamada Vendas com as seguintes colunas: Produto, Quantidade, PrecoUnitario e DataVenda. Você deseja criar uma medida que calcule a quantidade número de vendas para produtos que tenham sido vendidos por mais de _R$ 100,00._ 
```DAX
VendasAcimaDe100 = COUNTROWS(FILTER(Vendas, Vendas[PrecoUnitario] > 100))
```
Neste exemplo, temos o seguinte:

- `FILTER(Vendas, Vendas[PrecoUnitario] > 100)` filtra a tabela Vendas para incluir apenas as linhas onde o preço unitário do produto é superior a R$ 100,00.
- `COUNTROWS` conta o número de linhas resultantes da filtragem, ou seja, o número de vendas que atendem ao critério estabelecido.
  
A função FILTER é uma ferramenta poderosa no DAX para criar tabelas filtradas com base em condições específicas. Como uma função iteradora, ela avalia cada linha individualmente e retorna uma tabela contendo apenas as linhas que atendem à condição especificada. Compreender o funcionamento da FILTER, incluindo o conceito de contexto de linha, permite realizar análises avançadas e personalizadas no Power BI.



[↑ Voltar ao topo](#topo)

---
## 5. Destacando métricas
Conforme destacamos no [tópico anterior](#3-vendas-por-tipo-de-produto), a ideia de modificação em nosso DashBoard e aplicar um destaque para as vendas do tipo Ebook, deixando-os fixos, sem que sofram alterações ao clicar sobre algum filtro de nossas tabelas.  
Se analisarmos novamente nossa medida de vendas por Ebook,temo o filtro aplicado para a palavrá ebook, relacionada a tabela de produtos por tipo, vide exemplo abaixo:  
```DAX
Vendas Ebook = 
SUMX(
    FILTER( 
        Vendas,
        RELATED(Produtos[Tipo]) = "Ebook"
    ),
    Vendas[Quantidade] * Vendas[Preco Calculado]
)
```
felizmente existe uma funcionalidade DAX, que nos permite ignorar todos os filtros, e essa função trata-se da `ALL()`, Para não atrapalhar as medidas já construídas iremos adicionar mais uma medida.
```DAX
Vendas Ebook  ALL = 
SUMX(
    FILTER( 
        ALL(Vendas),
        RELATED(Produtos[Tipo]) = "Ebook"
    ),
    Vendas[Quantidade] * Vendas[Preco Calculado]
)
```
E como essa nossa nova medida se porta, se analisarmos a medida anterior realizamos a aplicação da função `FILTER()`, que tem em um dos seus argumentos, a passagem do parâmetro da tabela de busca/filtrada, porém com esse comportamento, caso fosse aplicado algum filtro na tabela de vendas, essa medida sofreria alterações em conjunto, para isso utilizamos a função `ALL()`, que nesse contexto irá ignorar os filtros aplicados e retornara todo o conteúdo da tabela, podemos conferir na prática a aplicação desse função na imagem abaixo:  

<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/funcao_all.png" alt="Função All " width="45%"/>
    </td>
</tr>
</table>

Conforme visualizamos na imagem, mesmo que haja um filtro incindo sobre alguma tabela essa medida não sofre alteração, aplicaremos agora a mesma lógicas para as demais medidas criadas para Ebook utilizado essa função, deixando agora em destaque em nosso DashBoard as medidas referentes ao produto de Ebook, conforme imagem abaixo:  

<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/cards_com_all.png" alt="Cards com All " width="45%"/>
    </td>
</tr>
</table>

> PS: Um adendo, na medida de `margem % all` utiliza uma função com duas medidas, para a utilização do `ALL()`, basta acrescentar a palavra all pós a medida.
> EX: `Margem Ebook % ALL = DIVIDE([Margem Ebook All],[Vendas Ebook  ALL],0)`

[↑ Voltar ao topo](#topo)

---
## 6. Para saber mais: RELATED e RELATEDTABLE

Na linguagem DAX, as funções `RELATED` e `RELATEDTABLE` desempenham um papel crucial ao lidar com relacionamentos entre tabelas. Elas permitem acessar e filtrar dados de tabelas relacionadas, facilitando análises complexas e integração de informações de diferentes fontes.

---

__Função RELATED__  

A função `RELATED` é usada para recuperar o valor de uma coluna em uma tabela relacionada com base em um relacionamento estabelecido. Ela funciona principalmente em contextos de filtro, onde o contexto de linha é propagado de uma tabela para outra através de um relacionamento.

Por exemplo, suponha que você tenha duas tabelas: Clientes e Pedidos. Se houver um relacionamento entre as tabelas Clientes e Pedidos usando a coluna IDCliente, você pode usar a função `RELATED` para recuperar informações sobre o cliente para cada pedido.  

---

__Função RELATEDTABLE__  

Por outro lado, a função `RELATEDTABLE` é usada para recuperar uma tabela inteira da tabela relacionada, em vez de apenas um valor específico. Ela retorna todas as linhas da tabela relacionada que correspondem ao contexto atual.

Essa função é útil quando você precisa acessar vários registros relacionados em uma tabela. Por exemplo, se quiser ver todos os pedidos feitos por um cliente específico, você pode usar a função `RELATEDTABLE` para retornar uma tabela com todos os pedidos desse cliente.  

---

__Principais diferenças__  
A principal diferença entre as duas funções é o tipo de valor retornado:

- A função `RELATED` retorna um valor escalar (um único valor) de uma coluna relacionada.
- A função `RELATEDTABLE` retorna uma tabela inteira contendo todas as linhas relacionadas.

---

__Função RELATED__  

A função `RELATED` utiliza o relacionamento _“*:1” (muitos para um)_ , pois a busca é feita a partir de uma tabela que pode conter vários registros de um mesmo item (muitos) com uma tabela que contém os registros únicos desses itens (um).

Por exemplo, podemos buscar os dados referentes a uma categoria de produto específica, como Data Science, a partir de uma tabela que contém vários registros de vendas desse mesmo produto. Nesse caso, estaríamos acessando um dado específico de outra tabela que corresponde a vários registros de vendas na tabela atual.

---

__Função RELATEDTABLE__  
A função `RELATEDTABLE`, por outro lado, parte de uma tabela inicial contendo registros únicos (um) para uma tabela que contém diversos registros sobre esse mesmo item da tabela inicial (muitos).

Seguindo a ideia do exemplo anterior, poderíamos calcular o total de vendas de cada categoria de produto, acessando as várias linhas de registros de vendas dos produtos de cada categoria. Com isso, estaríamos acessando vários registros de vendas sobre essa categoria específica em outra tabela, partindo de um tipo de categoria na tabela atual.

As funções `RELATED e RELATEDTABLE`  são ferramentas poderosas no toolkit do DAX para trabalhar com relacionamentos entre tabelas. Elas facilitam o acesso e a análise de dados em diferentes contextos, permitindo que você explore informações relacionadas de forma eficaz. Compreender como essas funções funcionam e como os relacionamentos entre tabelas são estabelecidos é essencial para criar análises avançadas e insights significativos com o Power BI.  

[↑ Voltar ao topo](#topo)

---
## 7. Filtrando regiões  
Em um contexto de uma loja de varejo que deseja analisar as vendas de seus produtos em diferentes regiões geográficas, utilizando o Power BI, você recebeu uma demanda onde será necessário criar uma medida que conte o número de vendas para a região "Norte".

Considerando esse cenário, qual das seguintes medidas é a correta para contar o número de vendas dessa região? Escolha a alternativa correta.
 
<table style="text-align: center; width: 100%;"> 
<tr>
    <td style="text-align: left;">
    <img src="imgs/Prova_Questoes/Resp_1.png" alt="Resposta Filtrando regiões" width="45%"/>
    </td>
</tr>
</table>

[↑ Voltar ao topo](#topo)

---
## 8. Mão na massa: calculando vendas com filtros  
Durante esta aula, exploramos algumas das poderosas funções do DAX, como FILTER, ALL e RELATED, que nos permitem manipular e analisar dados de forma eficaz no Power BI. Agora é hora de colocar seu conhecimento em prática com um desafio!

Você foi contratado(a) como analista de dados por uma empresa de varejo chamada "SuperVendas". Seu gerente solicitou um relatório que destaca o __desempenho das vendas em diferentes categorias de produtos durante o último trimestre__. Para isso, você deve criar uma medida que __calcule a receita total para a categoria "Data Science", ignorando quaisquer filtros aplicados nas visualizações.__

---
- Desafio:
  - Calcule a receita total para a categoria "Data Science" considerando todas as linhas da tabela.
  - Utilize a função FILTER para filtrar os dados apenas para a categoria.
  - Utilize a função RELATED para acessar a categoria na tabela de Produtos.
  - Utilize a função ALL para ignorar quaisquer filtros aplicados nas visualizações.
  
Em caso de dúvidas sobre a resolução da atividade, confira a seção "Opinião da pessoa instrutora".

__Opinião do instrutor__  

Para resolver este desafio, você pode seguir estes passos:

- Calcule a receita total para a categoria "Data Science" considerando todas as linhas da tabela.
- Utilize a função FILTER para filtrar os dados apenas para a categoria.
- Utilize a função RELATED para acessar a categoria na tabela de Produtos.
- Utilize a função ALL para ignorar quaisquer filtros aplicados nas visualizações.

Para fins didáticos, perceba a seguir um exemplo de como a medida pode ser criada:
```DAX
ReceitaDataScience = 
SUMX(
    FILTER(
        ALL(Vendas), 
        RELATED(Produtos[Categoria]) = "Data Science"
    ), 
    Vendas[Vendas Total]
)
```
Este código cria uma medida chamada "ReceitaDataScience" que utiliza a função FILTER para filtrar os dados apenas para a categoria "Data Science" e, em seguida, calcula a receita total para essa categoria, somando os valores de venda de todos os produtos eletrônicos.

Em caso de dúvidas, fique à vontade para usar o Fórum ou o Discord da Alura.

---
_Minha medida:_  

```DAX
DesafioMedida = SUMX(
    FILTER
        (ALL(Vendas),
        RELATED(Produtos[Categoria]) = "Data Science"
    ),
    Vendas[Quantidade] * Vendas[Preco Calculado]
)
```

[↑ Voltar ao topo](#topo)

---
## 9. O que aprendemos?

Nessa aula, você foi capaz de:  
- Conhecer as principais funções de tabela;
- Filtrar dados a partir da função FILTER();
- Remover filtros através da função ALL();
- Acessar colunas de outras tabelas com a função RELATED().

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
__Titulo:__ Funções de tabela
__Autor:__ Thierry Lucas Chaves  
__Data de Criação:__ 19-06-2026  
__Data de Modificação:__ 21-06-2026  
__Versão:__ "1.0"