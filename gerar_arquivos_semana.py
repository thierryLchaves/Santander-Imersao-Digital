import datetime
import re
import unicodedata
from pathlib import Path

# Constantes de Caminhos base usando pathlib de forma dinâmica
ROOT_DIR = Path(__file__).resolve().parent
BASE_DIR = ROOT_DIR / "Analise_de_dados_e_IA_Nivelamento"
README_PATH = ROOT_DIR / "README.md"
TEMPLATE_PATH = ROOT_DIR / "templates" / "template_aula.md"


def gerar_ancora(texto):
    link = texto.lower()
    # Remove pontuações (exceto espaços e hifens), mantendo letras acentuadas para o Github MD
    link = re.sub(r"[^\w\s-]", "", link)
    # Substitui espaços por hifens
    link = re.sub(r"\s+", "-", link)
    return link


def clean_text_for_folder(text):
    # Remove acentos para gerar nomes seguros
    text = unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("utf-8")
    # Remove caracteres especiais
    text = re.sub(r"[^\w\s]", "", text)
    # Substitui espaço por sublinhado para o Snake_Case
    return text.strip().replace(" ", "_")


def clean_text_for_file(text):
    text = unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("utf-8")
    words = re.sub(r"[^\w\s]", "", text).strip().split()
    # Retorna as palavras concatenadas em CamelCase
    return "".join(w.capitalize() for w in words) + ".md"


def parse_readme(semana):
    aulas_info = {}
    curso_atual = None
    curso_folder = None
    aula_folder = None
    aula_counter = 0

    try:
        with open(README_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Arquivo README não encontrado em: {README_PATH}")
        return {}

    in_semana = False
    for line in lines:
        # Identifica em qual semana estamos lendo
        if line.strip().startswith(f"### Semana - {semana}"):
            in_semana = True
            continue

        if in_semana:
            # Encerra leitura se encontrar a próxima semana ou o final do bloco
            if line.strip().startswith("### Semana -") or line.strip() == "</details>":
                break

            # Normaliza possíveis Tabs para 4 espaços p/ garantir leitura correta
            line = line.replace("\t", "    ")

            # Captura a indentação de espaços antes da tarefa `- [ ]`
            match = re.match(r"^(\s*)- \[[ xX]\] (.*)", line)
            if match:
                spaces = len(match.group(1))
                content = match.group(2).strip()

                # Remove marcações Markdown estéticas para não poluir os nomes de variáveis
                clean_content = re.sub(r"\*\*", "", content)
                clean_content = re.sub(
                    r"\[(.*?)\]\(.*?\)", r"\1", clean_content
                ).strip()

                if spaces == 0:
                    # Nível 1: Curso Principal / Módulo
                    curso_atual = clean_content
                    curso_folder = clean_text_for_folder(clean_content)
                    aula_counter = 0

                elif spaces == 4:
                    # Nível 2: Nome da Aula
                    aula_counter += 1
                    aula_atual = clean_content

                    aula_slug = clean_text_for_folder(clean_content)
                    aula_folder = f"{aula_counter:02d}_{aula_slug}"

                    aula_file = clean_text_for_file(clean_content)
                    # Checa automaticamente se devemos aplicar a badge do EXCEL
                    is_excel = (
                        "excel" in (curso_atual or "").lower()
                        or "excel" in aula_atual.lower()
                    )

                    path_key = Path(curso_folder) / aula_folder
                    aulas_info[path_key] = {
                        "arquivo": aula_file,
                        "titulo": aula_atual,
                        "is_excel": is_excel,
                        "topicos": [],
                    }

                elif spaces == 8:
                    # Nível 3: Tópicos dos vídeos
                    if curso_folder and aula_folder:
                        path_key = Path(curso_folder) / aula_folder
                        if path_key in aulas_info:
                            aulas_info[path_key]["topicos"].append(clean_content)

    return aulas_info


def criar_arquivos_md(semana, aulas_info):
    # Ler o conteúdo do template
    try:
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            template_content = f.read()
    except FileNotFoundError:
        print(f"Template não encontrado em: {TEMPLATE_PATH}")
        return

    data_atual = datetime.datetime.now().strftime("%d-%m-%Y")
    semana_folder = BASE_DIR / f"Semana_{semana}"

    for aula_path, info in aulas_info.items():
        arquivo_md = info["arquivo"]
        titulo_aula = info["titulo"]
        is_excel = info["is_excel"]
        topicos = info["topicos"]

        # Gera o Sumário e os blocos de conteúdo com ancoragem
        sumario_text = ""
        conteudo_text = ""
        for i, topico in enumerate(topicos, 1):
            ancora = f"{i}-{gerar_ancora(topico)}"
            sumario_text += f"- [{i}. {topico}](#{ancora})\n"
            conteudo_text += f"## {i}. {topico}\n\n[↑ Voltar ao topo](#topo)\n\n---\n"

        # Define o Badge
        badge_excel = (
            '\n    <td style="padding: 5px;">\n      <img alt="Microsoft Excel" src="https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white"/>\n    </td>'
            if is_excel
            else ""
        )

        # Prepara o conteúdo substituindo os placeholders
        conteudo = template_content.replace("[Nome da aula]", titulo_aula)
        conteudo = conteudo.replace("[SUMARIO_DINAMICO]", sumario_text.strip())
        conteudo = conteudo.replace("[CONTEUDO_DINAMICO]", conteudo_text.strip())
        conteudo = conteudo.replace("[BADGE_EXCEL]", badge_excel)
        conteudo = conteudo.replace("[DATA_ATUAL]", data_atual)

        caminho_pasta = semana_folder / aula_path
        caminho_arquivo = caminho_pasta / arquivo_md

        # Garante que a pasta existe antes de tentar criar o arquivo
        caminho_pasta.mkdir(parents=True, exist_ok=True)

        # Criação da estruturação de pastas de apoio (imgs, db, src) com .gitkeep
        for sub in ["imgs", "db", "src"]:
            sub_path = caminho_pasta / sub
            sub_path.mkdir(parents=True, exist_ok=True)
            (sub_path / ".gitkeep").touch()

        # Cria o arquivo .md na pasta correspondente
        with open(caminho_arquivo, "w", encoding="utf-8") as f:
            f.write(conteudo)

        print(f"Criado: {caminho_arquivo}")


if __name__ == "__main__":
    semana_input = input(
        "Digite o número da semana para processar do README (ex: 04): "
    ).strip()
    print(f"\nLendo o README.md para extrair a estrutura da Semana {semana_input}...\n")

    info_extraida = parse_readme(semana_input)

    if not info_extraida:
        print(
            "Nenhuma aula encontrada. Verifique se a '### Semana - X' no README.md existe e está identada com '- [ ]'"
        )
    else:
        criar_arquivos_md(semana_input, info_extraida)
        print(
            f"\nAutomação Concluída! Toda estrutura da Semana {semana_input} foi gerada com sucesso e sem Dicionários estáticos!"
        )
