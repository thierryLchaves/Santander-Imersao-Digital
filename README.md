# Santander Imersão Digital 
---
Este repositório tem como objetivo Realizar a documentação do material apreendido durante o curso de imersão Digital Santander + Alura.  
Nele serão arquivados materiais em **`Markdown`** para notações das aulas, caso necessário será criado um novo repositório com códigos e projetos etc..
## Sumário

* [1. Sobre a estrutura](#1-sobre-a-estrutura)
  * [1.1. Das pastas](#11-das-pastas)
    * [Estrutura padrão de sub-diretório](#11--estrutura-padrão-de-sub-diretório)
    * [1.1.1. Diretório de Imagens](#111-diretório-de-imagens)
    * [1.1.2. Diretório de Códigos](#112-diretório-de-códigos)
    * [1.1.3. Diretório de Dados](#113-diretório-de-dados)
  * [1.2. Do documento de anotações](#12-do-documento-de-anotações)
    * [1.2.1. Estrutura de rodapé](#121-estrutura-de-rodapé)
* [2. Lista de conclusão de aulas](#2-lista-de-conclusão-de-aulas)

### 1 Sobre a estrutura 
---
Conforme a estrutura do curso se da em trilhas e módulos, será adotado a seguinte formatação, as serão criadas **8 pastas** referentes as semanas, cada um conterá outras pastas com a tecnologia, abordada no curso, esses *`Sub Diretórios`*, seguirão o padrão `Snake_Case`, porém o nome dos arquivos serão em `CamelCase` com a referência da pasta o a aula em questão.   
- ### 1.1. Das pastas
    As pastas do curso terão um diretório base nomeado com base na trilha a ser estuada, já o seus *sub-diretórios*, irão se referir as semanas do conteúdo disponibilizado para estudo, 
    e os cursos do diretório terão um outro diretório com o nome ou resumo do curso realizado.
    - #### 1.1.  Estrutura padrão de sub-diretório
    Em toda pasta deverão conter no mínimo **3**(três) outros sub-diretórios  
    - #### 1.1.1. Diretório de Imagens
        `**Diretório de Imagens**`: Este diretório sempre será nomeado de `imgs`, e nele será armazenado os prints utilizados no documento.   
    - #### 1.1.2. Diretório de Códigos
        `**Diretório de código**`:  Este diretório sempre será nomeado de `src`, neste diretório será armazenado os exemplos de códigos feitos nas aulas e seguira a recomendação as boas práticas de  nomeação (sem upper case, com _ entre os nomes, e descrição curta do objetivo do código) 
    - #### 1.1.3. Diretório de Dados
        `**Diretório de dados*`: Este diretório sempre será nomeado de `db`, e nele será armazenado os dados complementares a serem usados (arquivos pdf etc..) 

- ### 1.2. Do documento de anotações
    Os documentos onde serão documentados os conhecimentos passados no curso terão em seu nome o *sub-titulo* do curso, facilitando a melhor compreensão, visto que a mesma tecnologia poderá ser abordada mais de uma vez dentro da trilha.
    Ao ser concluída uma nova aula deverá ser preenchido o [Check Box de conclusão](#2-lista-de-conclusão-de-aulas) informando que a aulas foi realizada.

    #### 1.2.1 Estrutura de rodapé
        Em todo arquivo deverá conter em seu rodapé a seguinte estrutura 
    ```
        <table style="text-align: center; width: 100%;"> 
        <caption><b>Skls do projeto </b></caption>
        <tr>
            <td style="text-align: center;">
            <img alt="Skil utilizada" src="buscar estilo em: https://github.com/Ileriayo/markdown-badges"/>
            </td>
        </tr>
        <tr> 
        <td style="text-align: center; width: 100%;">
        <b>Metadados</b>
        </td>
        </tr>
        </table>
        ---
        titulo: "Nome do documentos"
        autor: "Thierry Lucas Chaves"
        data_criacao: "DD-MM-AAAA"
        data_modificacao: "DD-MM-AAAA"
        versao: "1.0"
        ---
    ```

### 2. Lista de conclusão de aulas
> A medida que forem entendio as trilhas será realizado a criação dos checkbox para conclusão, bem como a adição de sumário.
- [ ]  <b> [Semana - 01](Analise_de_dados_e_IA_Nivelamento/Semana_01/)  </b>
    - [ ]  <b> [Excel: Domine o Editor de Planilhas](Analise_de_dados_e_IA_Nivelamento/Semana_01/Excel/Domine_o_editor_de_planilhas.md/)  </b>
        - <b> Conceitos </b>
            - [ ] Apresentação
            - [ ] Conhecendo o trabalho
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