import datetime
import re
import unicodedata
from pathlib import Path

# Constantes de Caminhos base usando pathlib de forma dinâmica
ROOT_DIR = Path(__file__).resolve().parent
BASE_DIR = ROOT_DIR / "Analise_de_dados_e_IA_Nivelamento"
README_PATH = ROOT_DIR / "README.md"
TEMPLATE_PATH = ROOT_DIR / "templates" / "template_aula.md"


def gerar_ancora(texto: str) -> str:
    link = texto.lower()
    # Remove pontuações (exceto espaços e hifens), mantendo letras acentuadas para o Github MD
    link = re.sub(r"[^\w\s-]", "", link)
    # Substitui espaços por hifens
    link = re.sub(r"\s+", "-", link)
    return link


def clean_text_for_folder(text: str) -> str:
    # Remove acentos para gerar nomes seguros
    text = unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("utf-8")
    # Remove caracteres especiais
    text = re.sub(r"[^\w\s]", "", text)
    # Substitui espaço por sublinhado para o Snake_Case
    return text.strip().replace(" ", "_")


def clean_text_for_file(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("utf-8")
    words = re.sub(r"[^\w\s]", "", text).strip().split()
    # Retorna as palavras concatenadas em CamelCase
    return "".join(w.capitalize() for w in words) + ".md"


def parse_readme(semana: str) -> dict:
    aulas_info = {}
    curso_atual = None
    curso_folder = None
    aula_counter = 0
    current_path_key = None

    try:
        with open(README_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Arquivo README não encontrado em: {README_PATH}")
        return {}

    in_semana = False
    for line in lines:
        # Identifica em qual semana estamos lendo
        if line.strip().startswith(f"### Semana - {semana}") or line.strip().startswith(
            f"### [Semana - {semana}"
        ):
            in_semana = True
            continue

        if in_semana:
            # Encerra leitura se encontrar a próxima semana ou o final do bloco
            if (
                line.strip().startswith("### Semana -")
                or line.strip().startswith("### [Semana -")
                or line.strip() == "</details>"
            ):
                break

            # Normaliza possíveis Tabs para 4 espaços p/ garantir leitura correta
            line = line.replace("\t", "    ")

            # Captura a indentação de espaços antes da tarefa `- [ ]` ou `- [x]`
            match = re.match(r"^(\s*)- \[[ xX]\] (.*)", line)
            if match:
                spaces = len(match.group(1))
                content = match.group(2).strip()

                # Remove marcações Markdown estéticas para não poluir os nomes
                clean_content = re.sub(r"\*\*", "", content)
                clean_content = re.sub(
                    r"\[(.*?)\]\(.*?\)", r"\1", clean_content
                ).strip()

                if spaces == 0:
                    # Nível 1: Curso Principal / Módulo
                    curso_atual = clean_content
                    curso_folder = clean_text_for_folder(clean_content)
                    aula_counter = 0
                    current_path_key = None

                elif spaces == 4:
                    # Nível 2: Nome da Aula
                    aula_counter += 1
                    aula_atual = clean_content

                    # Criação da pasta da aula em Snake_Case e o arquivo MD em CamelCase
                    aula_folder = (
                        f"{aula_counter:02d}_{clean_text_for_folder(clean_content)}"
                    )
                    aula_file = clean_text_for_file(clean_content)

                    # Checa automaticamente se devemos aplicar as badges
                    is_excel = (
                        "excel" in (curso_atual or "").lower()
                        or "excel" in aula_atual.lower()
                    )
                    is_powerbi = (
                        "power bi" in (curso_atual or "").lower()
                        or "powerbi" in (curso_atual or "").lower()
                        or "power bi" in aula_atual.lower()
                        or "powerbi" in aula_atual.lower()
                    )

                    if curso_folder:
                        # O mapeamento chave agora contempla as duas subpastas (Curso > Aula)
                        current_path_key = (curso_folder, aula_folder, aula_file)
                        aulas_info[current_path_key] = {
                            "titulo": aula_atual,
                            "is_excel": is_excel,
                            "is_powerbi": is_powerbi,
                            "topicos": [],
                        }

                elif spaces == 8:
                    # Nível 3: Tópicos dos vídeos
                    if current_path_key and current_path_key in aulas_info:
                        aulas_info[current_path_key]["topicos"].append(clean_content)

    return aulas_info


def criar_arquivos_md(semana: str, aulas_info: dict) -> None:
    # Ler o conteúdo do template
    try:
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            template_content = f.read()
    except FileNotFoundError:
        print(f"Template não encontrado em: {TEMPLATE_PATH}")
        return

    data_atual = datetime.datetime.now().strftime("%d-%m-%Y")
    semana_folder = BASE_DIR / f"Semana_{semana}"

    for path_key, info in aulas_info.items():
        curso_folder, aula_folder, arquivo_md = path_key
        titulo_aula = info["titulo"]
        is_excel = info["is_excel"]
        is_powerbi = info.get("is_powerbi", False)
        topicos = info["topicos"]

        # Gera o Sumário e os blocos de conteúdo com ancoragem
        sumario_text = ""
        conteudo_text = ""
        for i, topico in enumerate(topicos, 1):
            ancora = f"{i}-{gerar_ancora(topico)}"
            sumario_text += f"- [{i}. {topico}](#{ancora})\n"
            conteudo_text += f"## {i}. {topico}\n\n[↑ Voltar ao topo](#topo)\n\n---\n"

        # Define os Badges
        badge_excel = (
            '\n    <td style="padding: 5px;">\n      <img alt="Microsoft Excel" src="https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white"/>\n    </td>'
            if is_excel
            else ""
        )

        badge_powerbi = (
            '\n    <td style="padding: 5px;">\n      <img alt="Power BI" src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black"/>\n    </td>'
            if is_powerbi
            else ""
        )

        # Prepara o conteúdo substituindo os placeholders
        conteudo = template_content.replace("[Nome da aula]", titulo_aula)
        conteudo = conteudo.replace("[SUMARIO_DINAMICO]", sumario_text.strip())
        conteudo = conteudo.replace("[CONTEUDO_DINAMICO]", conteudo_text.strip())
        conteudo = conteudo.replace("[BADGE_EXCEL]", badge_excel)
        conteudo = conteudo.replace("[BADGE_POWERBI]", badge_powerbi)
        conteudo = conteudo.replace("[DATA_ATUAL]", data_atual)

        # Caminho refatorado (Trilha/Semana > Módulo/Curso > Aula > Arquivo)
        caminho_curso = semana_folder / curso_folder
        caminho_aula = caminho_curso / aula_folder
        caminho_arquivo = caminho_aula / arquivo_md

        # Garante que a pasta da aula existe antes de tentar criar o arquivo
        caminho_aula.mkdir(parents=True, exist_ok=True)

        # Criação da pasta de banco de dados (db) apenas na raiz do módulo, evitando redundância
        db_path = caminho_curso / "db"
        db_path.mkdir(parents=True, exist_ok=True)
        (db_path / ".gitkeep").touch(exist_ok=True)

        # Cria o arquivo .md na pasta da aula correspondente
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
