# 🤖 Prompt de Automação Semanal

**Para o Usuário Humano:**  
Sempre que começar uma nova semana de estudos, copie o texto puro contendo as aulas, cole substituindo o aviso na tag `<lista_bruta_da_semana>` abaixo e forneça o conteúdo deste arquivo para a sua IA (ex: Gemini). 
Assim que ela atualizar o `README.md`, execute o `gerar_arquivos_semana.py`. Ao final, apenas confirme com a IA para que ela gere os links.

---

## 🧠 INSTRUÇÕES PARA A LLM

Você atua como um engenheiro de software e assistente de documentação deste repositório.
Nós possuímos um script Python (`gerar_arquivos_semana.py`) que automatiza a criação de todas as pastas, diretórios de apoio (`imgs`, `db`, `src`), e gera os arquivos `.md` (populados com template, sumário interno, âncoras e badges).

**Sua função é assumir exclusivamente os passos de atualização que o script Python NÃO FAZ.** 
Por favor, siga os passos abaixo:

### Passo 1: Preparação do README.md
1. Leia o conteúdo fornecido na tag `<lista_bruta_da_semana>`.
2. Formate essa lista como caixas de seleção (`- [ ]`), preservando o aninhamento original (Trilha > Módulo > Aula > Tópico).
3. Envolva a lista gerada em uma tag `<details>` e adicione-a ao arquivo `README.md`, na seção **"5. Lista de conclusão de aulas"**.
4. Atualize o **Sumário** principal no topo do `README.md` adicionando o link/âncora para a nova semana.
5. IMPORTANTE: Sempre que realizar qualquer edição no `README.md`, não se esqueça de ir até o rodapé e atualizar a **Data de Modificação** para a data corrente, além de atualizar/incrementar a **Versão**.

<lista_bruta_da_semana>
Power BI Desktop: Construindo meu primeiro dashboard
  - Conectando os dados
    - Apresentação
    - Para saber mais: conta gratuita indisponível
    - Preparando o ambiente: Power BI e base de dados
    - Para saber mais: Business Intelligence
    - Construindo o cartão com a média de pets
    - Alinhamento configuração Power BI
    - Ajustando a visualização
    - Importando as pastas e mesclando as tabelas
    - Tipo de dado correto
    - Conectando com o Google planilhas
    - Renomeando tabelas
    - Faça como eu fiz
    - O que aprendemos?
  - Realizando Cálculos
    - Criando uma coluna calculada
    - Filtragem de dados nulos
    - Para saber mais: qualidade da coluna
    - Calculando o faturamento total
    - Calcular receita total das vendas
    - Para saber mais: medidas implícitas e explícitas
    - Para saber mais: M e DAX
    - Calculando o total de itens vendidos
    - Mão na massa: utilizando DAX
    - O que aprendemos?
  - Análises com os gráficos
    - Projeto da aula anterior
    - Trabalhando com o gráfico de pizza
    - Comparação de receita por gênero
    - Série temporal
    - Para saber mais: rótulos de hierarquia
    - Obtendo novos visuais
    - Visualizando imagens dos eventos
    - Faça como eu fiz: trazendo visuais externos
    - O que aprendemos?
  - Estilização do relatório 
    - Projeto da aula anterior
    - Estilização dos cartões
    - Ajustando imagem de fundo
    - Estilizando as segmentações
    - Para saber mais: apresentações de impacto
    - Estilizando o gráfico de pizza
    - Escolhendo visuais
    - Gráfico de área
    - Faça como eu fiz: dashboard com as estilizações
    - O que aprendemos?
  - Power Bi Service
    - Projeto da aula anterior
    - Layout móvel
    - Layout personalizado
    - Publicando na web
    - Para saber mais: publicar na web
    - Acessando o Power BI service
    - Fundo do dispositivo móvel
    - Faça como eu fiz: estilizando o layout móvel
    - Projeto final
    - Para ir mais fundo
    - O que aprendemos?
    - Conclusão
  
Power BI Desktop: Realizando ETL no Power Query
  - Conectando os datasets
    - Apresentação
    - Para saber mais: conta gratuita indisponível
    - Preparando o ambiente: Power BI Desktop
    - Conexão ao Excel e CSV
    - Avaliando a melhor base de dados
    - Conexão ao XML e JSON
    - Conhecendo o Power Query Editor
    - Mão na massa: explorando bases de dados da Olist
    - O que aprendemos?
  - Power Query Editor
    - Projeto da aula anterior
    - Extraindo textos
    - Mesclando consultas
    - Para saber mais: tipos de junção na mesclagem do Power BI
    - Traduzindo colunas
    - Possibilidades de transformações
    - Para saber mais: tratamento de dados com linguagem M
    - Trabalhando com delimitadores
    - Mão na massa: explorando a base com a coluna de exemplos
    - O que aprendemos?
  - Avançando nas transformações
    - Projeto da aula anterior
    - Transposição de tabela
    - Gerenciando parâmetros
    - Para saber mais: parâmetros
    - Organizando diretórios
    - Tipos dos dados
    - Evitando problemas futuros
    - Faça como eu fiz: inserindo parâmetros
    - O que aprendemos?
  - Finalizando os tratamento
    - Projeto da aula anterior
    - Renomeando e removendo consultas
    - Para saber mais: renomeando colunas no Power Query
    - Conhecendo o editor avançado
    - Para saber mais: diferença entre duplicar e referenciar uma tabela
    - Reaproveitando processos
    - Refatorando as etapas
    - Otimizando processos
    - Mão na massa
    - O que aprendemos?
  - Modelando os dados
    - Projeto da aula anterior
    - Carregando dados e acessando o modelo
    - Conhecendo as propriedades de relação
    - Escolhendo a cardinalidade
    - Para saber mais: a importância da modelagem de dados
    - Garantindo conexões assertivas
    - Modelando de forma adequada
    - Mão na massa
    - Projeto final
    - Referências
    - O que aprendemos?
    - Conclusão
</lista_bruta_da_semana>

### Passo 2: Aplicação dos Links
*Atenção: O usuário informará no chat quando o script Python tiver sido executado após o Passo 1.*

Quando a estrutura física já existir:
1. Modifique a lista de checkboxes adicionada no `README.md` no Passo 1.
2. Transforme os itens que representam **Módulos/Cursos** (nível 1 da lista) e **Aulas** (nível 2) em hiperlinks apontando para a estrutura física gerada.
3. Adote rigorosamente a regra do repositório:
   - Pastas formatadas em `Snake_Case` (e com subpastas numeradas `01_...`, `02_...`).
   - Arquivos Markdown formatados em `CamelCase`.

Aguarde minha confirmação após a execução do Passo 1 para avançarmos ao Passo 2!