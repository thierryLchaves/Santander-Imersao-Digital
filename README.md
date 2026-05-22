<a id="topo"></a>

# Santander Imersão Digital 

Este repositório tem como objetivo Realizar a documentação do material apreendido durante o curso de imersão Digital Santander + Alura.  
Nele serão arquivados materiais em __`Markdown`__ para anotações das aulas, caso necessário será criado um novo repositório com códigos e projetos etc..

## Sumário

- [Santander Imersão Digital](#santander-imersão-digital)
  - [Sumário](#sumário)
  - [1. Visão Geral](#1-visão-geral)
  - [2. Estrutura do Repositório](#2-estrutura-do-repositório)
    - [2.1 Organização das Pastas](#21-organização-das-pastas)
    - [2.2 Diretórios Padrão](#22-diretórios-padrão)
  - [3. Documentação e Padronização](#3-documentação-e-padronização)
    - [3.1 Estrutura de Rodapé](#31-estrutura-de-rodapé)
    - [3.2. Estrutura de Demarcação](#32-estrutura-de-demarcação)
    - [3.3 Exemplos de demarcações e efeitos](#33-exemplos-de-demarcações-e-efeitos)
    - [3.4. Ancoragem de Referência](#34-ancoragem-de-referência)
  - [4. Nomes dos documentos](#4-nomes-dos-documentos)
    - [4.1 Marcação de progresso](#41-marcação-de-progresso)
  - [5. Lista de conclusão de aulas](#5-lista-de-conclusão-de-aulas)
    - [Semana - 01](#semana---01)
    - [Semana - 02](#semana---02)
    - [Semana - 03](#semana---03)
---
## 1. Visão Geral
Conforme a estrutura do curso se dá em trilhas e módulos, adotaremos a seguinte formatação: serão criadas __8 pastas__ referentes às semanas. Cada uma conterá subdiretórios com a tecnologia abordada no curso de forma macro. Esses subdiretórios conterão outras pastas referentes às aulas do dia em questão. Ambos seguirão o padrão `Snake_Case`, porém os nomes dos arquivos serão em `CamelCase`, com referência à pasta ou à aula em questão.

[↑ Voltar ao topo](#topo)

---
## 2. Estrutura do Repositório

### 2.1 Organização das Pastas
As pastas seguem a cronologia das semanas (01 a 08). Cada sub-diretório representa a tecnologia abordada.
* **Sub-diretórios:** Nomeados em `Snake_Case`.
* **Arquivos:** Nomeados em `CamelCase` com referência à aula.

### 2.2 Diretórios Padrão
As pastas do curso terão um diretório base nomeado com base na trilha a ser estudada. Já os seus subdiretórios se referirão às semanas do conteúdo disponibilizado para estudo, e os cursos do diretório terão uma pasta com o nome ou resumo do curso realizado.
* **`imgs/` (Imagens):** Este diretório sempre será nomeado como `imgs`, e nele serão armazenados os prints utilizados no documento. As imagens a serem postadas nos documentos deverão seguir notação de `HTML`, podendo variar o alinhamento ou a proporção, conforme exemplo:
    ```html
        <table style="text-align: center; width: 100%;"> 
        <tr>
            <td style="text-align: left;">
            <img src="imgs/diagrama_internet.png" alt="Diagrama internet" width="45%"/>
            </td>
        </tr>
        </table>
    ```   
    Esse modelo se provou melhor tanto para apresentação quanto para persistência da informação nos documentos em `Markdown`, permitindo a inserção de imagens comparativas sem causar _overflow_ no documento.

* **`src/` (Códigos):** Este diretório sempre será nomeado como `src`. Nele serão armazenados os exemplos de códigos feitos nas aulas, seguindo as boas práticas de nomeação (sem *uppercase*, com `_` entre os nomes e descrição curta do objetivo do código).

* **`db/` (Dados):** Este diretório sempre será nomeado como `db`, e nele serão armazenados os dados complementares a serem usados (arquivos, PDF, bases de dados, Excel, CSV, etc.).

[↑ Voltar ao topo](#topo)

---
## 3. Documentação e Padronização
Para facilitar o processo de documentação, foi realizado a criação do [template](templates/template_aula.md), esse contém uma estrutura básica dessa dos documentos, o conteúdo desse template será copiado e editado conforme as anotações aconteçam.

### 3.1 Estrutura de Rodapé
Em todo arquivo deverá conter em seu rodapé a seguinte estrutura 

```html 
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

    __Titulo:__ Nome do Documento/Módulo
    __Autor:__ Thierry Lucas Chaves  
    __Data de Criação:__ DD-MM-YYYY  
    __Data de Modificação:__ DD-MM-YYYY  
    __Versão:__ "1.0"
```
Os badges serão modificados conforme a linguagem dos códigos a serem utilizados no curso, bem como as datas __DEVEM SER ATUALIZADAS__, seguindo a data de commit's feitos.
__PS:__ Caso necessário poderá ser utilizado o [repositório de badges](https://github.com/thierryLchaves/markdown-badges).  

[↑ Voltar ao topo](#topo)

### 3.2. Estrutura de Demarcação
Para manter a leitura organizada, siga estas convenções ao escrever:

* **Ênfase:** Use `__negrito__` para termos importantes e `_itálico_` para definições.
* **Código:** Utilize `código inline` para nomes de arquivos ou comandos rápidos. Para blocos de script, especifique a linguagem (ex: `sql`, `python`) para garantir o *syntax highlighting*.
* **Listas:** Sempre use o padrão de indentação de 2 espaços para subníveis.
* **Notas de Destaque:** Use o sinal `>` para citações ou notas de atenção (alertas de erro, dicas de performance).

[↑ Voltar ao topo](#topo)

### 3.3 Exemplos de demarcações e efeitos

- __Estrutura de tabela__
```Markdown
    Titulo da tabela
    |     |     |     |     |     |     | <!--Linha divisória do titulo com tabela --> |
    | --- | --- | --- | --- | --- | --- |<!--Quantidade de colunas a serem exibidas -->
    | A | B | C | D| F | G |
    | 1 | 2 | 3 | 4 | 5 | 6 |
```
Essa estrutura facilita as tabulações visto que se padronização conforme preenchimento do campo.

- __Marcações__ 
    - Para marcações de negrito ou itálico deve se utilizar o `_`, conforme exemplo abaixo 
    ```Markdown
        _Itálico_
        __Negrito__
        <u>Sublinhado</u>
    ```
- Para delimitações ou tópicos utilizaremos `---` , ao ser realizado o processo de limite ou demarcação de páginas, conforme demonstrado abaixo:

```Markdown
    Esse e um exemplo de utilização  
    ---
    Segue o conteúdo
```
- Listagem  
    A listas caso necessário serão realizadas utilizando o  processo da utilização de tabulação `TAB`, de onde está o parágrafo precedido de um `-`
facilitando assim a organização da notação, conforme demonstrado abaixo:

```Markdown
Lista de exemplo:  
    - tópico 1
    - tópico 2
    - tópico 3
    - tópico 4
```
- Títulos e subtítulos 
A estruturação dos  seguinte a premissa abaixo:

```Markdown
# Título principal (Nome do arquivo)
## Sub texto ou titulo de capitulo 
### Sub titulo ou marcações de tópicos
#### Sub divisão do anterior.
```
- Exemplos de código:
Esse processo será realizado de forma a utilizar o recurso de trecho de código demarcando a linguagem utilizada, em caso de incompatibilidade, não será determinado a linguagem, conforme demonstrado abaixo:

```Markdown

`*3Python
    def xpto
`*3
`*3 html
etc..
```
- Observações
Essas deverão ser precedidas de `>`, para melhor organização e destaque em página
- Tipos de arquivo 
    Será adotado durante as anotações, o modelo de __Inline code__, o que pode ser utilizado nesse repositório tanto para marcar que aquilo se trata de um tipo de arquivo ou linguagem de programação, quanto para demonstrar linhas de código simples ou comandos em uma determinada linguagem, simplificando a utilização do triplo __```__ e nome da linguagem.

### 3.4. Ancoragem de Referência
Quando for necessário realizar um ancoragem de resultados, seja para melhor legibilidade de resultados, ou para referências de conteúdos de lista será utilizado o código de links abaixo
```html
    <details id="ref01">
        <summary>Clique aqui para expandir (ou acesse via link)</summary>
            <p>Conteúdo que será revelado automaticamente!</p>
            <ul>
                <li>l1</li>
                <li> L2</li>
                <li> L3</li>
            </ul>
    </details>
```
Esse modelo realiza o processo de `collapse` do conteúdo. Ele deve ser utilizado em cenários como glossários, quando for necessário definir um termo desconhecido ou detalhar um conteúdo oculto. O código deve ser inserido abaixo do texto que contém o termo. Não seguiremos a premissa de `Inline Code` aqui, pois adicionaremos informações detalhadas sobre o assunto. Para realizar tal referência, utilizaremos o código abaixo:
```Markdown
<a href="#ref01">Ir para o ref01 e expandir</a>
```
[↑ Voltar ao topo](#topo)

## 4. Nomes dos documentos
Os documentos onde serão documentados os conhecimentos passados no curso terão em seu nome o mesmo nome do módulo do curso porém utilizando a estrutura de `SnakeCase`, facilitando padronização, e seguindo a definição estabelecida [aqui](#1-visão-geral), para além  disto essa estratégia foi adotada pois facilita a identificação da aula, conforme está estruturado na plataforma do curso.

### 4.1 Marcação de progresso
Ao ser concluída uma nova aula deverá ser preenchido o [Check Box de conclusão](#5-lista-de-conclusão-de-aulas) informando que a aula foi realizada, essa lista será preenchida seguindo a hierarquia:  

 1º Referência pasta do módulo da semana,
 2º Nome da trilha, e referência a pasta
 3º Nome do módulo da trilha e referência ao documento de anotações do módulo
 4º Listagem de todos os vídeos do módulo a sendo estudado

 [↑ Voltar ao topo](#topo)
   
## 5. Lista de conclusão de aulas
>À medida que forem estudadas as trilhas será realizado a criação dos checkbox para conclusão, bem como a adição de sumário.

### [Semana - 01](Analise_de_dados_e_IA_Nivelamento/Semana_01/)
<details>
  <summary><b> Aulas da Semana - 01</b></summary>

- [x] **[Excel: Domine o Editor de Planilhas](Analise_de_dados_e_IA_Nivelamento/Semana_01/Excel_domine_o_editor_de_planilhas/)**
    - [x] **[Conceitos do Excel](Analise_de_dados_e_IA_Nivelamento/Semana_01/Excel_domine_o_editor_de_planilhas/01_Domine_o_editor_de_planilhas/DomineOeditorDePlanilhas.md)**
        - [x] Apresentação
        - [x] Conhecendo o trabalho
        - [x] Conhecendo o `Excel`
        - [x] Inserindo linhas na planilha
        - [x] Organizando dados na planilha
        - [x] Edição e Formato
        - [x] Faça como fiz: *Digitando dados no `Excel`*
        - [x] Para saber mais: *Principais atalhos no `Excel`*
        - [x] O que aprendemos?
        - [x] Atividades

    - [x] **[Formatação passo a passo](Analise_de_dados_e_IA_Nivelamento/Semana_01/Excel_domine_o_editor_de_planilhas/02_Formatacao_passo_a_passo/FomatacaoPassoAPasso.md)**
        - [x] Preparando o ambiente: *planilha Meteora Ecommerce*
        - [x] Formatar como tabela
        - [x] Convertendo dados em tabela
        - [x] Aplicando formatos
        - [x] Inserindo dados em uma planilha formatada
        - [x] Faça como fiz: *Formatar como Moeda*
        - [x] O que aprendemos?

    - [x] **[Fórmulas e funções](Analise_de_dados_e_IA_Nivelamento/Semana_01/Excel_domine_o_editor_de_planilhas/03_Formulas_e_Funcoes/FormulasEFuncoes.md)**
        - [x] Preparando o ambiente: *planilha Meteora Ecommerce*
        - [x] Aplicando cálculos
        - [x] Calculando o total de vendas
        - [x] Tipos de referências
        - [x] Calculando o valor do desconto
        - [x] Faça como fiz: *Linha de totais*
        - [x] Desafio: *Valor do desconto*
        - [x] O que aprendemos?

    - [x] **[Estruturando os dados](Analise_de_dados_e_IA_Nivelamento/Semana_01/Excel_domine_o_editor_de_planilhas/04_Estruturando_os%20_dados/EstruturandoOsDados.MD)**
        - [x] Preparando o ambiente: *planilha Meteora Ecommerce*
        - [x] Resolvendo o primeiro desafio
        - [x] Estruturando a planilha
        - [x] Copiar o estilo de formatação
        - [x] Imprimindo a planilha
        - [x] Faça como fiz: *Ajustando o valor de desconto*
        - [x] O que aprendemos?

    - [x] **[Tornando os dados mais visuais](Analise_de_dados_e_IA_Nivelamento/Semana_01/Excel_domine_o_editor_de_planilhas/05_Tornando_os_dados_mais_visuais/TornandoOsDadosMaisVisuais.md)**
        - [x] Preparando o ambiente: *planilha Meteora Ecommerce*
        - [x] Criando gráficos
        - [x] Ajustando o Design de gráfico
        - [x] Adicionar elemento no gráfico
        - [x] Formatando o gráfico
        - [x] Faça como fiz: *Alterar o tipo de gráfico*
        - [x] O que aprendemos?

    - [x] **[Compartilhando dados na nuvem](Analise_de_dados_e_IA_Nivelamento/Semana_01/Excel_domine_o_editor_de_planilhas/06_Compartilhando_dados_na_nuvem/CompartilhandoDadosNaNuvem.md)**
        - [x] Preparando o ambiente: *planilha Meteora Ecommerce*
        - [x] Compartilhar e Colaborar
        - [x] Compartilhar o arquivo na nuvem
        - [x] Faça como fiz: *Salvando a planilha na nuvem*
        - [x] Explicando o desafio
        - [x] Desafio: *Calcular o desconto para cada produto*
        - [x] Projeto final do curso
        - [x] O que aprendemos?
        - [x] Conclusão

- [x] **[IA: Explorando o potencial da inteligência Artificial Generativa](Analise_de_dados_e_IA_Nivelamento/Semana_01/IA_explorando_o_potencial_da_inteligencia_artificial_generativa/)**

    - [x] **[IAs De Texto](Analise_de_dados_e_IA_Nivelamento/Semana_01/IA_explorando_o_potencial_da_inteligencia_artificial_generativa/01_IAs_De_Texto/IAsDeTexto.md)**
        - [x] Apresentação
        - [x] Usando o ChatGPT
        - [x] Descobrindo o Google Gemini
        - [x] Lidando com textos
        - [x] Aprimorando o contexto
        - [x] Mão na massa: Criando conteúdo para um blog de alimentação saudável
        - [x] Para saber mais
        - [x] O que aprendemos?

    - [x] **[Modelos de linguagem](Analise_de_dados_e_IA_Nivelamento/Semana_01/IA_explorando_o_potencial_da_inteligencia_artificial_generativa/02_Modelos_de_linguagem/ModelosDeLinguagem.md)**
        - [x] O que é e como funciona um modelo de linguagem
        - [x] Princípios da Engenharia de Prompt
        - [x] Análise de Prompts no ChatGPT
        - [x] Mão na massa: criando um post para seu trabalho
        - [x] Para saber mais
        - [x] O que aprendemos?

    - [x] **[IAs para análises](Analise_de_dados_e_IA_Nivelamento/Semana_01/IA_explorando_o_potencial_da_inteligencia_artificial_generativa/03_IAs_Para_Analises/IAsParaAnalises.md)**
        - [x] Análise de documentos
        - [x] Análise de imagens e vídeos
        - [x] Para saber mais: Sobre Tokens
        - [x] Análise de áudios
        - [x] Trabalhando com dados
        - [x] Mão na massa: analisando planilha e gerando gráficos
        - [x] Para saber mais: Mais ferramentas
        - [x] O que aprendemos?
    - [x] **[Geradores de imagens](Analise_de_dados_e_IA_Nivelamento/Semana_01/IA_explorando_o_potencial_da_inteligencia_artificial_generativa/04_Gerando_Imagens/GerandoImagens.md)**
        - [x] Bing Images e DALL-E
        - [x] Midjourney
        - [x] Prompts para imagens
        - [x] Mão na massa: completando post com imagens
        - [x] Para saber mais: Outras ferramentas
        - [x] O que aprendemos?
        - [x] Conclusão

</details>

---

### [Semana - 02](Analise_de_dados_e_IA_Nivelamento/Semana_02/)
<details>
  <summary><b>Aulas da Semana - 02</b></summary>

- [x] **[Funções com Excel: operações matemáticas e filtros](Analise_de_dados_e_IA_Nivelamento/Semana_02/Funcoes_com_excel_operacoes_matematicas_e_filtros/)**
    - [x] **[Classificando os dados no Excel](Analise_de_dados_e_IA_Nivelamento/Semana_02/Funcoes_com_excel_operacoes_matematicas_e_filtros/01_Classificando_os_dados_no_Excel/ClassificandoOsDadosNoExcel.md)**
      - [x] Apresentação
      - [x] Preparando o ambiente: Planilha Meteora E-commerce
      - [x] Classificação de Dados
      - [x] Classificação por níveis
      - [x] Outros tipos de classificação
      - [x] Faça como eu fiz: classificando os dados de produtos com tabela
      - [x] O que aprendemos?

    - [x] **[Aplicando filtros no Excel](Analise_de_dados_e_IA_Nivelamento/Semana_02/Funcoes_com_excel_operacoes_matematicas_e_filtros/02_Aplicando_filtros_no_Excel/AplicandoFiltrosNoExcel.MD)**
      - [x] Preparando o ambiente: planilha Meteora E-commerce
      - [x] Filtrando os dados
      - [x] Filtros específicos
      - [x] Filtro de número
      - [x] Filtro avançado
      - [x] Faça como eu fiz: filtrando os dados por categoria
      - [x] O que aprendemos?

    - [x] **[Cálculos com condição](Analise_de_dados_e_IA_Nivelamento/Semana_02/Funcoes_com_excel_operacoes_matematicas_e_filtros/03_Calculos_com_condicao/CalculosComCondicao.md)**
      - [x] Preparando o ambiente: planilha Meteora E-commerce
      - [x] Contando os produtos
      - [x] Contagem condicional
      - [x] Contagem de alunos
      - [x] Soma condicional
      - [x] Operadores lógicos
      - [x] Faça como eu fiz: contagem condicional
      - [x] O que aprendemos?
    - [x] **[Validação de dados](Analise_de_dados_e_IA_Nivelamento/Semana_02/Funcoes_com_excel_operacoes_matematicas_e_filtros/04_Validacao_de_dados/ValidacaoDeDados.md)**
      - [x] Preparando o ambiente: planilha Meteora E-commerce
      - [x] Explorando a Validação de Dados no Excel
      - [x] Criando uma validação de dados
      - [x] Tipos de mensagem
      - [x] Estilos de célula
      - [x] Faça como eu fiz: criando a lista de produtos
      - [x] O que aprendemos?

    - [x] **[Utilizando outras funções](Analise_de_dados_e_IA_Nivelamento/Semana_02/Funcoes_com_excel_operacoes_matematicas_e_filtros/05_Utilizando_outras_funcoes/UtilizandoOutrasfuncoes.md)**
      - [x] Preparando o ambiente: planilha Meteora E-commerce
      - [x] MÉDIA() e MÉDIASE()
      - [x] Média de gastos
      - [x] Faça como eu fiz: calculando a média do produtos
      - [x] Conhecendo o desafio
      - [x] Desafio: refazendo as funções com a tabela produtos
      - [x] Projeto final do curso
      - [x] O que aprendemos?
      - [x] Carreira em Excel
      - [x] Conclusão
      - [x] Créditos

- [x] **[Engenharia de Prompt: criando prompts eficazes para IA Generativas](Analise_de_dados_e_IA_Nivelamento/Semana_02/Engenharia_de_Prompt_criando_prompts_eficazes_para_IA_Generativa/)**
    - [x] **[Conceitos iniciais ](Analise_de_dados_e_IA_Nivelamento/Semana_02/Engenharia_de_Prompt_criando_prompts_eficazes_para_IA_Generativa/01_Conceitos_iniciais/ConceitosIniciais.md)**
        - [x] Apresentação
        - [x] Preparando o ambiente
        - [x] A proximidade semântica
        - [x] Word embeddings
        - [x] O que são tokens?
        - [x] Faça como eu fiz: explorando probabilidades
        - [x] O que aprendemos?

    - [x] **[Engenharia de Prompt](Analise_de_dados_e_IA_Nivelamento/Semana_02/Engenharia_de_Prompt_criando_prompts_eficazes_para_IA_Generativa/02_Engenharia_de_Prompt/EngenhariaDePrompt.md)**
        - [x] O que é Engenharia de Prompt?
        - [x] Para saber mais: motivando a ação
        - [x] Preparando o ambiente
        - [x] Princípios de criação
        - [x] Comunicando instruções
        - [x] Faça como eu fiz: princípios fundamentais
        - [x] O que aprendemos?

    - [x] **[Few-Shot Prompt](Analise_de_dados_e_IA_Nivelamento/Semana_02/Engenharia_de_Prompt_criando_prompts_eficazes_para_IA_Generativa/03_Few-Shot_Prompt/FewShotPrompt.md)**
        - [x] Preparando o ambiente
        - [x] Entendendo a técnica
        - [x] Mais exemplos
        - [x] Para saber mais: Few-Shot vs Zero-Shot
        - [x] Escolhendo técnicas
        - [x] Faça como eu fiz: comandos com exemplos
        - [x] O que aprendemos?

    - [x] **[Chain-of-Thougth Prompt](Analise_de_dados_e_IA_Nivelamento/Semana_02/Engenharia_de_Prompt_criando_prompts_eficazes_para_IA_Generativa/04_Chain-of-Thought_Prompt/ChainOfThoughtPrompt.md)**
        - [x] Preparando o ambiente
        - [x] Entendendo a técnica
        - [x] Outro exemplo
        - [x] Para saber mais: Zero-Shot com Chain of Thought
        - [x] Otimizando algoritmos
        - [x] Faça como eu fiz: cadeia de pensamentos
        - [x] O que aprendemos?

    - [x] **[Mais técnicas de Prompt](Analise_de_dados_e_IA_Nivelamento/Semana_02/Engenharia_de_Prompt_criando_prompts_eficazes_para_IA_Generativa/05_Mais_tecnicas_de_Prompt/MaisTecnicasDePrompt.md)**
        - [x] Least-to-Most Prompting
        - [x] Chain-of-Verification
        - [x] Self-Consistency
        - [x] Organizando processos
        - [x] Mão na massa: aplicando técnicas de Prompt no cotidiano
        - [x] O que aprendemos?
        - [x] Conclusão

</details>

---

### [Semana - 03](Analise_de_dados_e_IA_Nivelamento/Semana_03/)
<details>
  <summary><b>Aulas da Semana - 03</b></summary>

- [x] **[Recursos Visuais com Excel: explorando gráficos e formatos](Analise_de_dados_e_IA_Nivelamento/Semana_03/Recursos_visuais_com_excel_explorando_graficos_e_formatos/)**
    - [x] **[Formatação Condicional](Analise_de_dados_e_IA_Nivelamento/Semana_03/Recursos_visuais_com_excel_explorando_graficos_e_formatos/01_Formatacao_condicional/FormatacaoCondicional.md)**
        - [x] Apresentação
        - [x] Preparando o ambiente: planilha Meteora E-commerce
        - [x] Conhecendo o trabalho a ser feito
        - [x] Destaque com formatação condicional
        - [x] Conjunto de ícones e barras
        - [x] Classificando os dados em níveis
        - [x] Faça como eu fiz: conjunto de ícones
        - [x] O que aprendemos?

    - [x] **[Estruturando o dashboard](Analise_de_dados_e_IA_Nivelamento/Semana_03/Recursos_visuais_com_excel_explorando_graficos_e_formatos/02_Estruturando_o_dashboard/EstruturandoODashboard.md)**
        - [x] Projeto da aula anterior
        - [x] Estruturando o painel
        - [x] Criando indicadores
        - [x] Somando com uma condição
        - [x] Preparando os dados
        - [x] Faça como eu fiz: calculando os indicadores
        - [x] O que aprendemos?

    - [x] **[Trabalhando com gráficos](Analise_de_dados_e_IA_Nivelamento/Semana_03/Recursos_visuais_com_excel_explorando_graficos_e_formatos/03_Trabalhando_com_graficos/TrabalhandoComGraficos.md)**
        - [x] Projeto da aula anterior
        - [x] Criando um gráfico de barras
        - [x] Somando os dados mensais
        - [x] Somando com uma condição
        - [x] Gráfico de combinação
        - [x] Faça como eu fiz: gráfico de combinação
        - [x] O que aprendemos?

    - [x] **[Gráficos de relógio](Analise_de_dados_e_IA_Nivelamento/Semana_03/Recursos_visuais_com_excel_explorando_graficos_e_formatos/04_Graficos_de_relogio/GraficosDeRelogio.md)**
        - [x] Projeto da aula anterior
        - [x] Criando o gráfico de rosca
        - [x] Trabalhando com porcentagem
        - [x] Percentual de vendas
        - [x] Recursos de formatação
        - [x] Faça como eu fiz: gráfico de rosca
        - [x] Desafio: inserir a caixa de texto
        - [x] O que aprendemos?

    - [x] **[Concluindo o dashboard](Analise_de_dados_e_IA_Nivelamento/Semana_03/Recursos_visuais_com_excel_explorando_graficos_e_formatos/05_Concluindo_o_dashboard/ConcluindoODashboard.md)**
        - [x] Projeto da aula anterior
        - [x] Procura de valores
        - [x] Diferenciando as fórmulas
        - [x] Faça como eu fiz: corrigindo os valores na coluna ''Total''
        - [x] Explicando o desafio
        - [x] Desafio: alterando o tipo do gráfico
        - [x] Projeto final do curso
        - [x] O que aprendemos?
        - [x] Conclusão
        - [x] Créditos

- [X] **[ChatGPT: otimizando a qualidade dos resultados](Analise_de_dados_e_IA_Nivelamento/Semana_03/ChatGPT_otimizando_a_qualidade_dos_resultados/)**
    - [x] **[Criando os primeiros prompts](Analise_de_dados_e_IA_Nivelamento/Semana_03/ChatGPT_otimizando_a_qualidade_dos_resultados/01_Criando_os_primeiros_prompts/CriandoOsPrimeirosPrompts.md)**
        - [x] Apresentação
        - [x] Preparando o ambiente
        - [x] Para saber mais: compreendendo as limitações do ChatGPT - Por que nem sempre as respostas são precisas?
        - [x] Utilizando diferentes estratégias para criar prompts
        - [x] Para saber mais: entendendo o que são tokens
        - [x] Melhorando a qualidade das respostas
        - [x] Para saber mais: ChatGPT 3.5 vs ChatGPT 4 - Qual é a diferença?
        - [x] Desafio: crie um prompt com a técnica de conclusão
        - [x] O que aprendemos?

    - [x] **[Melhorando a confiabilidade dos resultados](Analise_de_dados_e_IA_Nivelamento/Semana_03/ChatGPT_otimizando_a_qualidade_dos_resultados/02_Melhorando_a_confiabilidade_dos_resultados/MelhorandoAConfiabilidadeDosResultados.md)**
        - [x] Dividindo tarefas complexas em subtarefas mais simples
        - [x] Aprendendo a dar instruções mais claras
        - [x] Para saber mais: boas práticas na escrita de prompts
        - [x] Maximizando o potencial dos resultados
        - [x] Utilizando boas práticas na criação de prompts
        - [x] Utilizando a estratégia Step by step
        - [x] Desafio: resolvendo um problema de lógica
        - [x] Queremos ouvir você!
        - [x] O que aprendemos?

    - [x] **[Explorando a aplicações](Analise_de_dados_e_IA_Nivelamento/Semana_03/ChatGPT_otimizando_a_qualidade_dos_resultados/03_Explorando_a_aplicacoes/ExplorandoAAplicacoes.md)**
        - [x] Sintetizando textos na linguagem correta: aprenda boas práticas
        - [x] Aprendendo a sintetizar resenhas de produto
        - [x] Traduzindo e sintetizando textos de forma eficiente
        - [x] Criando prompts para analisar sentimentos
        - [x] Para saber mais: Prompts - Diversas aplicações
        - [x] Desafio: analisando sentimentos em várias resenhas
        - [x] O que aprendemos?

    - [x] **[Estratégias para textos longos](Analise_de_dados_e_IA_Nivelamento/Semana_03/ChatGPT_otimizando_a_qualidade_dos_resultados/04_Estrategias_para_textos_longos/EstrategiasParaTextosLongos.md)**
        - [x] Trabalhando com textos longos
        - [x] Tentando resumir um texto com muitos caracteres
        - [x] Trabalhando com textos longos: system e message
        - [x] Para saber mais: o que é a OpenAI Playground?
        - [x] Desafio: resumindo um texto longo
        - [x] O que aprendemos?
        - [x] Conclusão
        - [x] Créditos

</details>

---
[↑ Voltar ao topo](#topo)

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
      <img alt="HTML5" src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"/>
    </td>
  </tr>
  <tr>
    <td style="padding: 5px;">
      <img alt="Microsoft Excel" src="https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white"/>
    </td>
    <td style="padding: 5px;">
      <img alt="Google Gemini" src="https://img.shields.io/badge/Google_Gemini-8E75B2?style=for-the-badge&logo=google-gemini&logoColor=white"/>
    </td>
  </tr>
</table>

---
__Titulo:__ Readme
__Autor:__ Thierry Lucas Chaves  
__Data de Criação:__ 23-04-2026  
__Data de Modificação:__ 20-05-2026  
__Versão:__ "2.3"