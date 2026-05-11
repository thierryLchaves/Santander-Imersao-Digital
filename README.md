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

- [X]  <b> [Semana - 01](Analise_de_dados_e_IA_Nivelamento/Semana_01/)  </b>
    - [X] <b> [Excel: Domine o Editor de Planilhas](Analise_de_dados_e_IA_Nivelamento/Semana_01/Excel_domine_o_editor_de_planilhas/)</b>
        - [X] <b> [Conceitos do Excel](Analise_de_dados_e_IA_Nivelamento/Semana_01/Excel_domine_o_editor_de_planilhas/01_Domine_o_editor_de_planilhas/DomineOeditorDePlanilhas.md) </b>
            - [X] Apresentação
            - [X] Conhecendo o trabalho
            - [X] Conhecendo o `Excel`
            - [X] Inserindo linhas na planilha
            - [X] Organizando dados na planilha
            - [X] Edição e Formato
            - [X] Faça como fiz: *Digitando dados no `Excel`*
            - [X] Para saber mais: *Principais atalhos no `Excel`*
            - [X]  O que aprendemos?
            - [X] Atividades

        - [X] <b> [Formatação passo a passo](Analise_de_dados_e_IA_Nivelamento/Semana_01/Excel_domine_o_editor_de_planilhas/02_Formatacao_passo_a_passo/FomatacaoPassoAPasso.md) </b>
            - [X] Preparando o ambiente: *planilha Meteora Ecommerce*
            - [X] Formatar como tabela
            - [X] Convertendo dados em tabela
            - [X] Aplicando formatos
            - [X] Inserindo dados em uma planilha formatada
            - [X] Faça como fiz: *Formatar como Moeda*
            - [X] O que aprendemos?

        - [X] <b> [Fórmulas e funções](Analise_de_dados_e_IA_Nivelamento/Semana_01/Excel_domine_o_editor_de_planilhas/03_Formulas_e_Funcoes/FormulasEFuncoes.md) </b>
            - [X] Preparando o ambiente: *planilha Meteora Ecommerce*
            - [X] Aplicando cálculos
            - [X] Calculando o total de vendas
            - [X] Tipos de referências 
            - [X] Calculando o valor do desconto
            - [X] Faça como fiz: *Linha de totais*
            - [X] Desafio: *Valor do desconto*
            - [X] O que aprendemos?

        - [X] <b> [Estruturando os dados](Analise_de_dados_e_IA_Nivelamento/Semana_01/Excel_domine_o_editor_de_planilhas/04_Estruturando_os%20_dados/EstruturandoOsDados.MD) </b>
            - [X] Preparando o ambiente: *planilha Meteora Ecommerce*
            - [X] Resolvendo o primeiro desafio
            - [X] Estruturando a planilha
            - [X] Copiar o estilo de formatação
            - [X] Imprimindo a planilha
            - [x] Faça como fiz: *Ajustando o valor de desconto*
            - [X] O que aprendemos?

        - [X] <b> [Tornando os dados mais visuais](Analise_de_dados_e_IA_Nivelamento/Semana_01/Excel_domine_o_editor_de_planilhas/05_Tornando_os_dados_mais_visuais/TornandoOsDadosMaisVisuais.md) </b>
            - [X] Preparando o ambiente: *planilha Meteora Ecommerce*
            - [X] Criando gráficos
            - [x] Ajustando o Design de gráfico
            - [X] Adicionar elemento no gráfico
            - [X] Formatando o gráfico
            - [X] Faça como fiz: *Alterar o tipo de gráfico*
            - [X] O que aprendemos?

        - [X] <b> [Compartilhando dados na nuvem](Analise_de_dados_e_IA_Nivelamento/Semana_01/Excel_domine_o_editor_de_planilhas/06_Compartilhando_dados_na_nuvem/CompartilhandoDadosNaNuvem.md) </b>
            - [X] Preparando o ambiente: *planilha Meteora Ecommerce*
            - [X] Compartilhar e Colaborar
            - [X] Compartilhar o arquivo na nuvem
            - [X] Faça como fiz: *Salvando a planilha na nuvem*
            - [X] Explicando o desafio
            - [X] Desafio: *Calcular o desconto para cada produto*
            - [X] Projeto final do curso
            - [X] O que aprendemos?
            - [X] Conclusão

    - [X]  <b> [IA: Explorando o potencial da inteligência Artificial Generativa](Analise_de_dados_e_IA_Nivelamento/Semana_01/IA_explorando_o_potencial_da_inteligencia_artificial_generativa/)  </b>

        - [X] <b> [IAs De Texto](Analise_de_dados_e_IA_Nivelamento/Semana_01/IA_explorando_o_potencial_da_inteligencia_artificial_generativa/01_IAs_De_Texto/IAsDeTexto.md) </b>
            - [X] Apresentação
            - [X] Usando o ChatGPT
            - [X] Descobrindo o Google Gemini
            - [X] Lidando com textos
            - [X] Aprimorando o contexto
            - [X] Mão na massa: Criando conteúdo para um blog de alimentação saudável
            - [X] Para saber mais
            - [X] O que aprendemos?

        - [X] <b> [Modelos de linguagem](Analise_de_dados_e_IA_Nivelamento/Semana_01/IA_explorando_o_potencial_da_inteligencia_artificial_generativa/02_Modelos_de_linguagem/ModelosDeLinguagem.md) </b>
            - [X] O que é e como funciona um modelo de linguagem
            - [X] Princípios da Engenharia de Prompt
            - [X] Análise de Prompts no ChatGPT
            - [X] Mão na massa: criando um post para seu trabalho
            - [X] Para saber mais
            - [X] O que aprendemos? 

        - [X] <b> [IAs para análises](Analise_de_dados_e_IA_Nivelamento/Semana_01/IA_explorando_o_potencial_da_inteligencia_artificial_generativa/03_IAs_Para_Analises/IAsParaAnalises.md) </b>
            - [X] Análise de documentos
            - [X] Análise de imagens e vídeos
            - [X] Para saber mais: Sobre Tokens
            - [X] Análise de áudios
            - [X] Trabalhando com dados
            - [X] Mão na massa: analisando planilha e gerando gráficos
            - [X] Para saber mais: Mais ferramentas
            - [X] O que aprendemos?
        - [X] <b> [Geradores de imagens](Analise_de_dados_e_IA_Nivelamento/Semana_01/IA_explorando_o_potencial_da_inteligencia_artificial_generativa/04_Gerando_Imagens/GerandoImagens.md) </b>
            - [X] Bing Images e DALL-E
            - [X] Midjourney
            - [X] Prompts para imagens
            - [X] Mão na massa: completando post com imagens
            - [X] Para saber mais: Outras ferramentas
            - [X] O que aprendemos?
            - [X] Conclusão
---
- [ ]  <b> [Semana - 02](Analise_de_dados_e_IA_Nivelamento/Semana_02/)  </b>
    - [ ] <b> [Funções com Excel: operações matemáticas e filtros](Analise_de_dados_e_IA_Nivelamento/Semana_02/Funcoes_com_excel_operacoes_matematicas_e_filtros/)</b>
        -[X] <b> [Classificando os dados no Excel](Analise_de_dados_e_IA_Nivelamento/Semana_02/Funcoes_com_excel_operacoes_matematicas_e_filtros/01_Classificando_os_dados_no_Excel/ClassificandoOsDadosNoExcel.md) </b>
          - [X] Apresentação
          - [X] Preparando o ambiente: Planilha Meteora E-commerce
          - [X] Classificação de Dados
          - [X] Classificação por níveis
          - [X] Outros tipos de classificação
          - [X] Faça como eu fiz: classificando os dados de produtos com tabela
          - [X] O que aprendemos?
        - [ ] <b>[Aplicando filtros no Excel](Analise_de_dados_e_IA_Nivelamento/Semana_02/Funcoes_com_excel_operacoes_matematicas_e_filtros/02_Aplicando_filtros_no_Excel/AplicandoFiltrosNoExcel.MD) </b>
          - [ ] Preparando o ambiente: planilha Meteora E-commerce
          - [ ] Filtrando os dados
          - [ ] Filtros específicos
          - [ ] Filtro de número
          - [ ] Filtro avançado
          - [ ] Faça como eu fiz: filtrando os dados por categoria
          - [ ] O que aprendemos?

        - [ ] <b> [Cálculos com condição](Analise_de_dados_e_IA_Nivelamento/Semana_02/Funcoes_com_excel_operacoes_matematicas_e_filtros/03_Calculos_com_condicao/CalculosComCondicao.md) </b>
          - [ ] Preparando o ambiente: planilha Meteora E-commerce
          - [ ] Contando os produtos
          - [ ] Contagem condicional
          - [ ] Contagem de alunos
          - [ ] Soma condicional
          - [ ] Operadores lógicos
          - [ ] Faça como eu fiz: contagem condicional
          - [ ] O que aprendemos?
        - [ ] <b> [Validação de dados](Analise_de_dados_e_IA_Nivelamento/Semana_02/Funcoes_com_excel_operacoes_matematicas_e_filtros/04_Validacao_de_dados/ValidacaoDeDados.md) </b>
          - [ ] Preparando o ambiente: planilha Meteora E-commerce
          - [ ] Explorando a Validação de Dados no Excel
          - [ ] Criando uma validação de dados
          - [ ] Tipos de mensagem
          - [ ] Estilos de célula
          - [ ] Faça como eu fiz: criando a lista de produtos
          - [ ] O que aprendemos?

        - [ ] <b> [Utilizando outras funções](Analise_de_dados_e_IA_Nivelamento/Semana_02/Funcoes_com_excel_operacoes_matematicas_e_filtros/05_Utilizando_outras_funcoes/UtilizandoOutrasfuncoes.md) </b>
          - [ ] Preparando o ambiente: planilha Meteora E-commerce
          - [ ] MÉDIA() e MÉDIASE()
          - [ ] Média de gastos
          - [ ] Faça como eu fiz: calculando a média do produtos
          - [ ] Conhecendo o desafio
          - [ ] Desafio: refazendo as funções com a tabela produtos
          - [ ] Projeto final do curso
          - [ ] O que aprendemos?
          - [ ] Carreira em Excel
          - [ ] Conclusão
          - [ ] Créditos

    - [ ] <b> [Engenharia de Prompt: criando prompts eficazes para IA Generativas](Analise_de_dados_e_IA_Nivelamento/Semana_02/Engenharia_de_Prompt_criando_prompts_eficazes_para_IA_Generativa/)</b>
        -[ ] <b> [Conceitos iniciais ](Analise_de_dados_e_IA_Nivelamento/Semana_02/Engenharia_de_Prompt_criando_prompts_eficazes_para_IA_Generativa/01_Conceitos_iniciais/ConceitosIniciais.md) </b>
            - [ ] Apresentação
            - [ ] Preparando o ambiente
            - [ ] A proximidade semântica
            - [ ] Word embeddings
            - [ ] O que são tokens?
            - [ ] Faça como eu fiz: explorando probabilidades
            - [ ] O que aprendemos?

        -[ ] <b> [Engenharia de Prompt](Analise_de_dados_e_IA_Nivelamento/Semana_02/Engenharia_de_Prompt_criando_prompts_eficazes_para_IA_Generativa/02_Engenharia_de_Prompt/EngenhariaDePrompt.md) </b>
            - [ ] O que é Engenharia de Prompt?
            - [ ] Para saber mais: motivando a ação
            - [ ] Preparando o ambiente
            - [ ] Princípios de criação
            - [ ] Comunicando instruções
            - [ ] Faça como eu fiz: princípios fundamentais
            - [ ] O que aprendemos?

        -[ ] <b> [Few-Shot Prompt](Analise_de_dados_e_IA_Nivelamento/Semana_02/Engenharia_de_Prompt_criando_prompts_eficazes_para_IA_Generativa/03_Few-Shot_Prompt/FewShotPrompt.md) </b>
            - [ ] Preparando o ambiente
            - [ ] Entendendo a técnica
            - [ ] Mais exemplos
            - [ ] Para saber mais: Few-Shot vs Zero-Shot
            - [ ] Escolhendo técnicas
            - [ ] Faça como eu fiz: comandos com exemplos
            - [ ] O que aprendemos?

        -[ ] <b> [Chain-of-Thougth Prompt](Analise_de_dados_e_IA_Nivelamento/Semana_02/Engenharia_de_Prompt_criando_prompts_eficazes_para_IA_Generativa/04_Chain-of-Thought_Prompt/ChainOfThoughtPrompt.md) </b>
            - [ ] Preparando o ambiente
            - [ ] Entendendo a técnica
            - [ ] Outro exemplo
            - [ ] Para saber mais: Zero-Shot com Chain of Thought
            - [ ] Otimizando algoritmos
            - [ ] Faça como eu fiz: cadeia de pensamentos
            - [ ] O que aprendemos?

        -[ ] <b> [Mais técnicas de Prompt](Analise_de_dados_e_IA_Nivelamento/Semana_02/Engenharia_de_Prompt_criando_prompts_eficazes_para_IA_Generativa/05_Mais_tecnicas_de_Prompt/MaisTecnicasDePrompt.md) </b>
            - [ ] Least-to-Most Prompting
            - [ ] Chain-of-Verification
            - [ ] Self-Consistency
            - [ ] Organizando processos
            - [ ] Mão na massa: aplicando técnicas de Prompt no cotidiano
            - [ ] O que aprendemos?
            - [ ] Conclusão


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
</table>

---
__Titulo:__ Readme
__Autor:__ Thierry Lucas Chaves  
__Data de Criação:__ 23-04-2026  
__Data de Modificação:__ 07-05-2026  
__Versão:__ "2.0"