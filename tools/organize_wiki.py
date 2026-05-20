#!/usr/bin/env python3
"""Organize wiki pages into consistent topical categories.

The wiki is intentionally kept as a flat directory (see WIKI_SCHEMA.md). This
script normalizes each page's category metadata and rebuilds wiki/index.md so
files are discoverable by topic without moving immutable raw sources.
"""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI_DIR = ROOT / "wiki"
INDEX_FILE = WIKI_DIR / "index.md"
LOG_FILE = WIKI_DIR / "log.md"

CATEGORY_ORDER = [
    "Fontes base",
    "Visão Computacional",
    "Agent Skills e Automação",
    "Carreiras e Mercado de Trabalho",
    "Computação Quântica e Criptografia",
    "Bioinformática e Biotech",
    "Cibersegurança",
    "Sustentabilidade e ESG",
    "Tecnologia Emergente",
    "Saúde",
    "Finanças",
    "Geral",
]

MANUAL_PAGES = {
    "Explicacao_YOLO_Parametros.md": (
        "Explicação dos Parâmetros do YOLO",
        "Resumo dos parâmetros base do modelo YOLO (confiança, IoU, bounding box).",
    ),
    "Deteccao_Objetos_YOLO_Python.md": (
        "Detecção de Objetos Usando YOLO e Python",
        "Workflow completo para treino de um modelo YOLOv8 no Colab com Roboflow.",
    ),
    "Projeto_Sistemas_Multiagentes.md": (
        "Projeto de Sistemas Multiagentes",
        "Integração YOLO, CrewAI e Gemini para relatórios de rastreamento visual.",
    ),
    "Reconhecimento_Yolo_OpenCV.md": (
        "Reconhecimento de objetos com YOLO e OpenCV",
        "Como aplicar o OpenCV com YOLOv8 nano para inferência em imagens e vídeos.",
    ),
}


def extract_title(text: str, fallback: str) -> str:
    frontmatter_title = re.search(r"^title:\s*(.+)$", text, re.MULTILINE)
    if frontmatter_title:
        return frontmatter_title.group(1).strip().strip('"')
    heading = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if heading:
        return heading.group(1).strip()
    return Path(fallback).stem


def category_for(title: str, filename: str) -> str:
    value = f"{title} {filename}".casefold()

    if any(
        term in value
        for term in ["yolo", "opencv", "computer vision", "visão", "vision"]
    ):
        return "Visão Computacional"
    if any(term in value for term in ["quantum", "quântic", "post-quantum"]):
        return "Computação Quântica e Criptografia"
    if any(
        term in value
        for term in [
            "bioinformatic",
            "biotechnology",
            "biotech",
            "life science",
            "lifescience",
            "zageno",
        ]
    ):
        return "Bioinformática e Biotech"
    if any(term in value for term in ["cybersecurity", "cyber security"]):
        return "Cibersegurança"
    if any(
        term in value
        for term in [
            "stanford emerging technology",
            "emerging technology",
            "technology review",
        ]
    ):
        return "Tecnologia Emergente"
    if any(
        term in value
        for term in [
            "green job",
            "green credential",
            "green economy",
            "sustainab",
            "esg",
            "renew & sustain",
            "renew _ sustain",
        ]
    ):
        return "Sustentabilidade e ESG"
    if "health care" in value or "healthcare" in value:
        return "Saúde"
    if "quant finance" in value or "finance careers" in value:
        return "Finanças"
    if any(
        term in value
        for term in [
            "career",
            "job",
            "labor",
            "labour",
            "talent",
            "workforce",
            "workplace",
            "employer",
            "reskilling",
            "skill gap",
            "skills in demand",
            "higher education",
        ]
    ):
        return "Carreiras e Mercado de Trabalho"
    if any(
        term in value
        for term in [
            "agent skill",
            "claude",
            "gemini",
            "openclaw",
            "codex-skills",
            "skyone",
            " skill",
            "skills",
        ]
    ):
        return "Agent Skills e Automação"
    return "Geral"


def normalize_category(text: str, category: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            frontmatter = text[:end]
            rest = text[end:]
            if re.search(r"^category:\s*.+$", frontmatter, re.MULTILINE):
                frontmatter = re.sub(
                    r"^category:\s*.+$",
                    f"category: {category}",
                    frontmatter,
                    flags=re.MULTILINE,
                )
            else:
                frontmatter = f"{frontmatter}\ncategory: {category}"
            text = frontmatter + rest
    text = re.sub(
        r"^\*\*Categoria:\*\*\s*.+$",
        f"**Categoria:** {category}",
        text,
        flags=re.MULTILINE,
    )
    return text


def build_index(entries: dict[str, list[tuple[str, str, str]]]) -> str:
    lines = [
        "# Wiki Index",
        "",
        "Catálogo organizado por tema para localizar rapidamente as páginas da base de conhecimento.",
        "",
        "## Categorias",
        "",
    ]
    for category in CATEGORY_ORDER:
        category_entries = sorted(
            entries.get(category, []), key=lambda item: item[0].casefold()
        )
        if not category_entries:
            continue
        lines.extend([f"### {category}", ""])
        for title, filename, description in category_entries:
            suffix = f" - {description}" if description else ""
            lines.append(f"- [{title}]({filename}){suffix}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    entries: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for page in sorted(WIKI_DIR.glob("*.md")):
        if page.name in {INDEX_FILE.name, LOG_FILE.name}:
            continue
        text = page.read_text(encoding="utf-8", errors="ignore")
        if page.name in MANUAL_PAGES:
            title, description = MANUAL_PAGES[page.name]
            category = "Fontes base"
        else:
            title = extract_title(text, page.name)
            description = ""
            category = category_for(title, page.name)
            normalized = normalize_category(text, category)
            if normalized != text:
                page.write_text(normalized, encoding="utf-8")
        entries[category].append((title, page.name, description))

    INDEX_FILE.write_text(build_index(entries), encoding="utf-8")


if __name__ == "__main__":
    main()
