#!/usr/bin/env python3
"""Valida o pacote sem dependências externas."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REQUIRED = ("## Contrato operacional v4", "## Saída v4")

def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("frontmatter ausente")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("frontmatter sem fechamento")
    fields = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields, text

def main():
    errors = []
    dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    manifest_names = set(manifest["skills"])
    dir_names = {p.name for p in dirs}
    if manifest_names != dir_names:
        errors.append("manifest.json não corresponde aos diretórios de skills")
    names = set()
    for folder in dirs:
        path = folder / "SKILL.md"
        if not path.exists():
            errors.append(f"{folder.name}: SKILL.md ausente")
            continue
        try:
            fields, text = frontmatter(path)
        except ValueError as exc:
            errors.append(f"{path}: {exc}")
            continue
        name = fields.get("name", "")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            errors.append(f"{path}: nome inválido: {name}")
        if name in names:
            errors.append(f"nome duplicado: {name}")
        names.add(name)
        if not fields.get("description"):
            errors.append(f"{path}: description ausente")
        for section in REQUIRED:
            if section not in text:
                errors.append(f"{path}: seção obrigatória ausente: {section}")
        if "TODO" in text or "TBD" in text or "PLACEHOLDER" in text:
            errors.append(f"{path}: placeholder não resolvido")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print(f"OK: {len(dirs)} skills, manifest e contratos estruturais válidos")
    return 0

if __name__ == "__main__":
    sys.exit(main())
