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
Power BI: Construindo cálculos com Dax
  - Conhecendo os dados
     - Apresentação
     - Para saber mais: conta gratuita indisponível
     - Preparando o ambiente
     - Para saber mais: roadmap do curso
     - Importando os dados
     - Para saber mais: modelo semântico no Power BI
     - Explorando o DAX
     - Para saber mais: básico do DAX
     - Calculando o desconto com DAX
     - Mão na massa: explorando as bases de dados
     - O que aprendemos?
  - Colunas calculadas e medidas
     - Projeto da aula anterior
     - Calculando o Total de Vendas
     - Para saber mais: ferramentas DAX
     - Calculando a Margem
     - Porcentagem da Margem
     - Para saber mais: colunas calculadas e medidas
     - Para saber mais: medidas rápidas, implícitas e explícitas
     - Aprimorando os cálculos
     - Para saber mais: funções iteradoras
     - Calculando a receita média
     - Mão na massa: criando medidas com funções iteradoras
     - O que aprendemos?
  - Funções de tabela
     - Projeto da aula anterior
     - Vendas por categoria
     - Vendas por tipo de produto
     - Para saber mais: função FILTER
     - Destacando métricas
     - Para saber mais: RELATED e RELATEDTABLE
     - Filtrando regiões
     - Mão na massa: calculando vendas com filtros
     - O que aprendemos?
  - Contextos no DAX
     - Projeto da aula anterior
     - Contexto de filtro
     - Contexto de linha
     - Para saber mais: Contexto de filtro X Contexto de linha
     - Combinando contextos
     - Avaliando contextos no DAX
     - Mão na massa: explorando os contextos no DAX
     - O que aprendemos?
  - Conhecendo o CALCULATE
     - Projeto da aula anterior
     - Vendas por vendedores
     - Para saber mais: criando a tabela calendário
     - Mudando o contexto de filtro
     - Para saber mais: transição de contexto
     - Filtrando com CALCULATE
     - Para saber mais: funções de filtro
     - Mão na massa: criando uma matriz
     - O que aprendemos?
  - Inteligência temporal
     - Projeto da aula anterior
     - Tabela calendário
     - Para saber mais: funções de DATA
     - Calculando o período anterior
     - Para saber mais: funções de inteligência temporal
     - Calculando a diferença das vendas
     - Vendas do período anterior
     - Mão na massa: relatório final
     - Projeto final
     - Para ir mais fundo
     - O que aprendemos?
     - Conclusão

Power BI: Visualizando e analisando dados
  - Analisando categorias
     - Apresentação
     - Para saber mais: conta gratuita indisponível
     - Preparando o ambiente
     - Explorando os dados
     - Identificando a melhor forma de visualização
     - Refletindo sobre o gráfico de pizza
     - Para saber mais: usos do gráfico de pizza
     - Análise com gráfico de pizza
     - Faça como eu fiz: crie uma hierarquia
     - O que aprendemos?
  - Selecionando visuais para categorias 
     - Projeto da aula anterior
     - Adicionando guias de análises
     - Configure uma dica de ferramenta
     - Para saber mais: dicas de ferramenta (Tooltips) no Power BI
     - Utilize um parâmetro de campo
     - Otimizando análises no Power BI com parâmetros de campo
     - Faça como eu fiz: praticando com o parâmetro
     - O que aprendemos?
  - Analisando dados ao longo do tempo
     - Projeto da aula anterior
     - Criando gráfico de linha e área
     - Identifique tendências
     - Para saber mais: aprimorando a análise com detecção de anomalias e previsões no Power BI
     - Detecte anomalias e faça previsões
     - Decifrando o faturamento da Opuline
     - Faça como eu fiz: trabalhando com tendências e previsões
     - O que aprendemos?
  - Monitorando  outros indicadores
     - Projeto da aula anterior
     - Visualize dados em mapas
     - Acompanhe os KPIs
     - Para saber mais: aprimorando o monitoramento de KPIs no Power BI
     - Monitore as metas
     - Visualizando metas na Clínica Médica Voll
     - Revele padrões com gráficos de dispersão
     - Faça como eu fiz: entendendo a correlação entre duas categorias
     - O que aprendemos?
  - Estruturando o relatório 
     - Projeto da aula anterior
     - Trabalhando com temas
     - Aplicando a identidade visual da Opuline
     - Inserindo o layout final
     - Para saber mais: seleção e indicadores
     - Finalizando página de vendas
     - Estilizando página de produtos
     - Navegação entre botões
     - Para saber mais: menu sanduíche
     - Mão na massa: estruture uma apresentação
     - Para saber mais: aprimorando o design e a navegação de relatórios
     - Faça como eu fiz: utilizando botões para navegação
     - Projeto final
     - Para ir mais fundo
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