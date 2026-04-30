# Santander Imersão Digital 

Este repositório tem como objetivo Realizar a documentação do material apreendido durante o curso de imersão Digital Santander + Alura.  
Nele serão arquivados materiais em __`Markdown`__ para notações das aulas, caso necessário será criado um novo repositório com códigos e projetos etc..


## Sumário

* [1. Sobre a Estrutura](#1-sobre-a-estrutura)
    * [1.1. Organização das Pastas](#11-das-pastas)
        * [Estrutura Padrão de Sub-diretórios](#11--estrutura-padrão-de-sub-diretório)
        * [1.1.1. Diretório de Imagens (imgs)](#111-diretório-de-imagens)
        * [1.1.2. Diretório de Códigos (src)](#112-diretório-de-códigos)
        * [1.1.3. Diretório de Dados (db)](#113-diretório-de-dados)
    * [1.2. Documentação de Anotações](#12-do-documento-de-anotações)
        * [1.2.1. Estrutura de Rodapé](#121-estrutura-de-rodapé)
        * [1.2.2. Padronização de Demarcação](#122-estrutura-de-demarcação)
* [2. Lista de Conclusão de Aulas](#2-lista-de-conclusão-de-aulas)
    * [2.1. Semana 01 - Análise de Dados e IA](#2-lista-de-conclusão-de-aulas)

### 1 Sobre a estrutura 
---
Conforme a estrutura do curso se da em trilhas e módulos, será adotado a seguinte formatação, as serão criadas __8 pastas__ referentes as semanas, cada um conterá outras pastas com a tecnologia, abordada no curso, esses _`Sub Diretórios`_ , seguirão o padrão `Snake_Case`, porém o nome dos arquivos serão em `CamelCase` com a referência da pasta o a aula em questão.   
- ### 1.1. Das pastas
    As pastas do curso terão um diretório base nomeado com base na trilha a ser estuada, já o seus *sub-diretórios*, irão se referir as semanas do conteúdo disponibilizado para estudo, 
    e os cursos do diretório terão um outro diretório com o nome ou resumo do curso realizado.
    - #### 1.1.  Estrutura padrão de sub-diretório
    Em toda pasta deverão conter no mínimo __3__(três) outros sub-diretórios  
    - #### 1.1.1. Diretório de Imagens
        __`Diretório de Imagens`__: Este diretório sempre será nomeado de `imgs`, e nele será armazenado os prints utilizados no documento., 
        as imagens a serem postas nos documentos deverão seguir notação de `HTML`, conforme exemplo:  
        ```html
            <table style="text-align: center; width: 100%;"> 
            <tr>
                <td style="text-align: left;">
                <img src="imgs/diagrama_internet.png" alt="Diagrama internetf" width="45%"/>
                </td>
            </tr>
            </table>
        ```   
        Esse modelo se provou melhor tanto para apresentação quanto para persistência da informação nos documentos em __`Markdown`__, para além da melhor visualização das imagens e organização caso necessário a inserção de mais de uma imagem para efeitos comparativos e evitar overflow no documento
    - #### 1.1.2. Diretório de Códigos
        __`Diretório de código`__:  Este diretório sempre será nomeado de `src`, neste diretório será armazenado os exemplos de códigos feitos nas aulas e seguira a recomendação as boas práticas de  nomeação (sem upper case, com _ entre os nomes, e descrição curta do objetivo do código) 
    - #### 1.1.3. Diretório de Dados
        __`Diretório de dados`__: Este diretório sempre será nomeado de `db`, e nele será armazenado os dados complementares a serem usados (arquivos pdf etc..) 

- ### 1.2. Do documento de anotações
    Os documentos onde serão documentados os conhecimentos passados no curso terão em seu nome o *sub-titulo* do curso, facilitando a melhor compreensão, visto que a mesma tecnologia poderá ser abordada mais de uma vez dentro da trilha.
    Ao ser concluída uma nova aula deverá ser preenchido o [Check Box de conclusão](#2-lista-de-conclusão-de-aulas) informando que a aulas foi realizada.

    #### 1.2.1 Estrutura de rodapé
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

    #### 1.2.2 Estrutura de demarcação
    Caso necessário utilizar marcações tabulares, ou demais estruturas de marcações também seguiram uma padronização em suas utilizações, sendo essas listadas abaixo:

    - __Estrutura de tabela__
    ```Markdown
        Titulo da tabela
        | | | | | | | <!--Linha divisória do titulo com tabela -->
        | -- | -- | -- | -- | -- | -- | <!--Quantidade de colunas a serem exibidas -->
        | A | B | C | D| F | G |
        | 1 | 2 | 3 | 4 | 5 | 6 |
    ```
    Essa estrutura facilita as tabulações visto que se padronização conforme preenchimento do campo.
    - __Marcações__ 
        - Para marcações de negrito ou itálico deve se utilizar o `_`, conforme exemplo abaixo 
        ```Markdown
            _Itálico_
            __Negrito__
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


### 2. Lista de conclusão de aulas
> A medida que forem entendio as trilhas será realizado a criação dos checkbox para conclusão, bem como a adição de sumário.
- [ ]  <b> [Semana - 01](Analise_de_dados_e_IA_Nivelamento/Semana_01/)  </b>
    - [ ]  <b> [Excel: Domine o Editor de Planilhas](Analise_de_dados_e_IA_Nivelamento/Semana_01/Excel/Domine_o_editor_de_planilhas.md/)  </b>
        - <b> Conceitos </b>
            - [X] Apresentação
            - [X] Conhecendo o trabalho
            - [ ] Conhecendo o `Excel`
            - [ ] Inserindo linhas na planilha
            - [ ] Organizando dados na planilha
            - [ ] Edição e Formato
            - [ ] Faça como fiz: *Digitando dados no `Excel`*
            - [ ] Para saber mais: *Principais atalhos no `Excel`*
            - [ ] O que aprendemos ? 
            - [ ] Atividades

        - <b> Formatação passo a passo </b>
            - [ ] Preparando o ambiente: *planilha Meteora Ecommerce*
            - [ ] Formatar como tabela
            - [ ] Convertendo dados em tabela
            - [ ] Aplicando formatos
            - [ ] Inserindo dados em uma planilha formatada
            - [ ] Faça como fiz: *Formatar como Moeda*
            - [ ] O que aprendemos ?

        - <b> Fórmulas e funções </b>
            - [ ] Preparando o ambiente: *planilha Meteora Ecommerce*
            - [ ] Aplicando cálculos
            - [ ] Calculando o total de vendas
            - [ ] Tipos de referências 
            - [ ] Calculando o valor do desconto
            - [ ] Faça como fiz: *Linha de totais*
            - [ ] Desafio: *Valor do desconto*
            - [ ] O que aprendemos ?

        - <b> Estruturando os dados</b>
            - [ ] Preparando o ambiente: *planilha Meteora Ecommerce*
            - [ ] Resolvendo o primeiro desafio
            - [ ] Estruturando a planilha
            - [ ] Copiar o estilo ed formatação
            - [ ] Imprimindo a planilha
            - [ ] Faça como fiz: *Ajustando o valor de desconto*
            - [ ] O que aprendemos ?

        - <b> Tornando os dados mais visuais </b>
            - [ ] Preparando o ambiente: *planilha Meteora Ecommerce*
            - [ ] Criando gráficos
            - [ ] Ajustando o Design de gráfico
            - [ ] Adicionar elemento no gráfico
            - [ ] Faça como fiz: *Alterar o tipo de gráfico*
            - [ ] O que aprendemos ? 

        - <b> Compartilhando dados na nuvem </b>
            - [ ] Preparando o ambiente: *planilha Meteora Ecommerce*
            - [ ] Compartilhar e Colaborar
            - [ ] Compartilhar o arquivo na nuvem
            - [ ] Faça como fiz: *Salvando a planilha na nuvem*
            - [ ] Explicando o desafio
            - [ ] Desafio: *Calcular o desconto para caa produto*
            - [ ] Projeto final o curso
            - [ ] O que aprendemos ?
            - [ ] Conclusão

    - [ ]  <b> [IA: Explorando o potencial da inteligência Artificial Generativa](Analise_de_dados_e_IA_Nivelamento/Semana_01/IA/Explorando_o_potencial_da_inteligencia_artificial_generativa.md)  </b>
        - <b> Conceitos </b>
            - [ ] Apresentação
            - [ ] Usando o ChatGPT
            - [ ] Descobrindo o Google Gemini
            - [ ] Lidando com Textos
            - [ ] Aprimorando o contexto
            - [ ] Mão na massa: *Criando conteúdo para um blog de alimentação saudável*
            - [ ] Para saber mais
            - [ ] O que aprendemos ? 
            - [ ] Atividades

        - <b> Modelos de linguagem </b>
            - [ ] O que é e como funciona um modelo de linguagem ?
            - [ ] Princípios de Engenharia de prompt
            - [ ] Análises de prompts no ChatGpt
            - [ ] Mão na massa: *Criando um post para seu trabalho*
            - [ ] Para saber mais
            - [ ] O que aprendemos ?

        - <b> IAs para análises </b>
            - [ ] Análise de documentos
            - [ ] Análise de imagens e vídeos
            - [ ] Pra saber mais: *Sobre Tokens*
            - [ ] Análise de áudios
            - [ ] Trabalhando com dados
            - [ ] Mão na massa: *Analisando planilha e gerando gráficos*
            - [ ] Para saber mais: *Mais ferramentas*
            - [ ] O que aprendemos ?

        - <b> Geradores de imagens </b>
            - [ ] Bing Imagens e DALL-E
            - [ ] Midjourney
            - [ ] Prompts para imagens
            - [ ] Mão na massa: *Completando post com imagens*
            - [ ] O que aprendemos ?
            - [ ] Conclusão