""" 
scripts/init_quarto_stubs.py
------------------------------

Script to initialize Quarto stubs for reports.
"""

from pathlib import Path
import re

REPORTS_DIR = Path("reports")

def title_from_filename(path: Path) -> str:
    name = path.stem.replace("_", " ").replace("-", " ").title()
    return name

def has_front_matter(text: str) -> bool:
    return text.lstrip().startswith("---")

def generate_index_body(title: str) -> str:
    return f"""---
title: "{title}"
---

This section presents materials related to **{title}**.

Subsections provide detailed analysis, supporting data,
and relevant discussion for this topic.
"""

def generate_page_body(title: str) -> str:
    return f"""---
title: "{title}"
---

<!--
TODO:
- Add objectives
- Describe data and methodology
- Insert analysis and figures
-->
"""

def main():
    qmd_files = REPORTS_DIR.rglob("*.qmd")

    for file in qmd_files:
        text = file.read_text(encoding="utf-8")

        if has_front_matter(text):
            continue  # Don't overwrite existing content

        title = title_from_filename(file)

        if file.name == "index.qmd":
            new_text = generate_index_body(title)
        else:
            new_text = generate_page_body(title)

        file.write_text(new_text, encoding="utf-8")
        print(f"Initialized: {file}")

if __name__ == "__main__":
    main()
