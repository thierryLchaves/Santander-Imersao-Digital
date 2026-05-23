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
[HUMANO: COLE AQUI A LISTA BRUTA DE MÓDULOS E AULAS DA NOVA SEMANA]
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