#!/usr/bin/env python3
"""Install the AI Specialist Skill Pack into a repository.

The installer intentionally uses only Python's standard library so it can run
on macOS, Linux, and Windows without first installing dependencies.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path


PACK_ROOT = Path(__file__).resolve().parent
LOCK_DIR = ".ai-specialist-pack"
LOCK_FILE = f"{LOCK_DIR}/pack.lock.json"
START_MARKER = "<!-- ai-specialist-pack:start -->"
END_MARKER = "<!-- ai-specialist-pack:end -->"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_manifest() -> dict:
    path = PACK_ROOT / "manifest.json"
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def source_files(profile: str) -> list[tuple[Path, str]]:
    manifest = load_manifest()
    files: list[tuple[Path, str]] = []
    for skill_name in manifest["profiles"][profile]:
        source = PACK_ROOT / "skills" / skill_name / "SKILL.md"
        if not source.is_file():
            raise RuntimeError(f"Skill ausente: {source}")
        files.append((source, f".agents/skills/{skill_name}/SKILL.md"))

    references_root = PACK_ROOT / "references"
    for source in sorted(references_root.rglob("*")):
        if source.is_file():
            relative = source.relative_to(references_root).as_posix()
            files.append((source, f".agents/references/{relative}"))
    return files


def agents_block() -> str:
    instructions = (PACK_ROOT / "AI_SPECIALIST.md").read_text(encoding="utf-8").strip()
    return f"{START_MARKER}\n{instructions}\n{END_MARKER}"


def update_agents(repo: Path, dry_run: bool) -> tuple[str, bool]:
    path = repo / "AGENTS.md"
    block = agents_block()
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    start = existing.find(START_MARKER)
    end = existing.find(END_MARKER)

    if start >= 0 and end >= start:
        end += len(END_MARKER)
        updated = existing[:start] + block + existing[end:]
    elif start >= 0 or end >= 0:
        raise RuntimeError("AGENTS.md contém marcadores incompletos do pack")
    elif existing:
        updated = existing.rstrip() + "\n\n" + block + "\n"
    else:
        updated = block + "\n"

    changed = updated != existing
    if changed and not dry_run:
        path.write_text(updated, encoding="utf-8")
    return "AGENTS.md", changed


def parse_args(argv: list[str]) -> argparse.Namespace:
    commands = {"install", "update", "migrate", "validate", "uninstall"}
    command = "install"
    remaining = argv[:]
    if remaining and remaining[0] in commands:
        command = remaining.pop(0)

    parser = argparse.ArgumentParser(
        description="Instala e gerencia o AI Specialist Skill Pack em um repositório."
    )
    parser.add_argument("repo", nargs="?", help="raiz do repositório alvo")
    parser.add_argument("--source", type=Path, default=PACK_ROOT, help="origem do pack")
    parser.add_argument(
        "--profile",
        choices=("standard", "ai", "delivery", "full"),
        help="perfil de skills a instalar (padrão: standard)",
    )
    parser.add_argument("--dry-run", action="store_true", help="mostra mudanças sem escrever")
    parser.add_argument("--force", action="store_true", help="sobrescreve conflitos de arquivos")
    parser.add_argument("--with-config", action="store_true", help="cria config.example.json")
    parser.add_argument("--yes", action="store_true", help="confirma a remoção")
    args = parser.parse_args(remaining)
    args.command = command
    if not args.repo:
        parser.error("informe o caminho do repositório")
    args.repo = Path(args.repo).expanduser().resolve()
    args.source = args.source.expanduser().resolve()
    return args


def copy_pack(args: argparse.Namespace) -> int:
    global PACK_ROOT
    if args.source != PACK_ROOT:
        PACK_ROOT = args.source

    repo = args.repo
    if not repo.is_dir():
        print(f"ERRO: repositório não encontrado: {repo}", file=sys.stderr)
        return 1

    manifest = load_manifest()
    lock_path = repo / LOCK_FILE
    existing_lock = None
    if lock_path.is_file():
        existing_lock = json.loads(lock_path.read_text(encoding="utf-8"))

    if args.command == "migrate" and existing_lock:
        if existing_lock.get("version") == manifest["version"]:
            print("ERRO: a instalação já usa a versão atual; use update.", file=sys.stderr)
            return 1
        stale = remove_locked_files(repo, existing_lock, args.dry_run)
        if stale:
            print("Arquivos legados removidos:" if not args.dry_run else "Arquivos legados que seriam removidos:")
            print("\n".join(f"  - {item}" for item in stale))

    if args.command == "update" and existing_lock:
        old_version = existing_lock.get("version")
        if old_version and old_version != manifest["version"]:
            print(
                f"ERRO: instalação {old_version} detectada; use migrate antes de update.",
                file=sys.stderr,
            )
            return 1

    profile = args.profile
    if profile is None:
        profile = existing_lock.get("profile", "standard") if args.command == "update" and existing_lock else "standard"
    if profile not in manifest["profiles"]:
        print(f"ERRO: perfil inválido: {profile}", file=sys.stderr)
        return 1
    files = source_files(profile)
    selected_paths = {relative for _, relative in files}
    conflicts: list[str] = []
    changes: list[str] = []
    for source, relative in files:
        destination = repo / relative
        if destination.exists() and sha256(destination) != sha256(source):
            conflicts.append(relative)
        elif not destination.exists():
            changes.append(f"criar {relative}")

    if conflicts and not args.force:
        print("ERRO: arquivos conflitantes (use --force para substituir):")
        print("\n".join(f"  - {item}" for item in conflicts))
        return 1

    stale_removed, stale_preserved = remove_stale_files(
        repo, existing_lock, selected_paths, args.dry_run
    )
    if stale_removed:
        changes.extend(
            ("atualizar " if args.dry_run else "remover ") + item
            for item in stale_removed
        )
    if stale_preserved:
        changes.extend("preservar " + item for item in stale_preserved)

    for source, relative in files:
        destination = repo / relative
        if args.dry_run:
            if not destination.exists() or relative in conflicts:
                changes.append(f"atualizar {relative}" if relative in conflicts else f"criar {relative}")
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)

    agents_relative, agents_changed = update_agents(repo, args.dry_run)
    if agents_changed:
        changes.append("atualizar " + agents_relative)

    config_path = repo / LOCK_DIR / "config.example.json"
    if args.with_config and not config_path.exists():
        config = {
            "project": {"name": "", "stack": [], "entrypoints": []},
            "commands": {"build": [], "test": [], "lint": [], "deploy": []},
            "constraints": {"production_access": "ask", "sensitive_paths": []},
            "integrations": []
        }
        if not args.dry_run:
            config_path.parent.mkdir(parents=True, exist_ok=True)
            config_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
        changes.append("criar " + str(config_path.relative_to(repo)))

    if not args.dry_run:
        managed = {
            relative: sha256(repo / relative) for _, relative in files
        }
        lock = {
            "pack": "ai-specialist-skill-pack",
            "version": manifest["version"],
            "profile": profile,
            "source": str(args.source),
            "managed_files": managed,
            "agents_markers": [START_MARKER, END_MARKER]
        }
        lock_path = repo / LOCK_FILE
        lock_path.parent.mkdir(parents=True, exist_ok=True)
        lock_path.write_text(json.dumps(lock, indent=2) + "\n", encoding="utf-8")

    print(
        f"Pack {manifest['version']} ({profile}) "
        f"{'seria instalado' if args.dry_run else 'instalado'} em {repo}"
    )
    if changes:
        print("Mudanças:")
        print("\n".join(f"  - {item}" for item in changes))
    else:
        print("Nenhuma mudança necessária.")
    return 0


def remove_locked_files(repo: Path, lock: dict, dry_run: bool) -> list[str]:
    removed: list[str] = []
    for relative, expected_hash in lock.get("managed_files", {}).items():
        path = repo / relative
        if not path.is_file() or sha256(path) != expected_hash:
            continue
        if not dry_run:
            path.unlink()
        removed.append(relative)
    return removed


def remove_stale_files(
    repo: Path,
    lock: dict | None,
    selected_paths: set[str],
    dry_run: bool,
) -> tuple[list[str], list[str]]:
    if not lock or lock.get("version") != load_manifest()["version"]:
        return [], []
    removed: list[str] = []
    preserved: list[str] = []
    for relative, expected_hash in lock.get("managed_files", {}).items():
        if relative in selected_paths:
            continue
        path = repo / relative
        if not path.is_file():
            continue
        if sha256(path) != expected_hash:
            preserved.append(relative)
            continue
        if not dry_run:
            path.unlink()
        removed.append(relative)
    return removed, preserved


def validate_installation(args: argparse.Namespace) -> int:
    repo = args.repo
    lock_path = repo / LOCK_FILE
    if not lock_path.is_file():
        print(f"ERRO: lock não encontrado: {lock_path}", file=sys.stderr)
        return 1
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    manifest = load_manifest()
    profile = lock.get("profile", "standard")
    if profile not in manifest["profiles"]:
        print(f"ERRO: perfil desconhecido no lock: {profile}", file=sys.stderr)
        return 1
    missing = [path for path in lock["managed_files"] if not (repo / path).is_file()]
    if missing:
        print("ERRO: arquivos ausentes:")
        print("\n".join(f"  - {item}" for item in missing))
        return 1
    print(f"OK: pack {lock['version']} ({profile}) instalado e completo em {repo}")
    return 0


def uninstall(args: argparse.Namespace) -> int:
    if not args.yes and not args.dry_run:
        print("ERRO: use --yes para confirmar a remoção", file=sys.stderr)
        return 1
    lock_path = args.repo / LOCK_FILE
    if not lock_path.is_file():
        print("Nenhuma instalação registrada encontrada.")
        return 0
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    preserved: list[str] = []
    removed: list[str] = []
    for relative, expected_hash in lock["managed_files"].items():
        path = args.repo / relative
        if not path.exists():
            continue
        if sha256(path) != expected_hash:
            preserved.append(relative)
            continue
        if not args.dry_run:
            path.unlink()
        removed.append(relative)

    agents = args.repo / "AGENTS.md"
    if agents.exists():
        content = agents.read_text(encoding="utf-8")
        start = content.find(START_MARKER)
        end = content.find(END_MARKER)
        if start >= 0 and end >= start:
            end += len(END_MARKER)
            updated = content[:start].rstrip() + content[end:]
            if not args.dry_run:
                agents.write_text(updated.lstrip() + ("\n" if updated.strip() else ""), encoding="utf-8")
            removed.append("AGENTS.md: bloco do pack")

    if not args.dry_run:
        lock_path.unlink(missing_ok=True)
        try:
            lock_path.parent.rmdir()
        except OSError:
            # Keep config.example.json or other user-created files.
            pass
    print(f"{'Seriam removidos' if args.dry_run else 'Removidos'}: {len(removed)} itens")
    if preserved:
        print("Preservados por terem sido modificados localmente:")
        print("\n".join(f"  - {item}" for item in preserved))
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.command in {"install", "update", "migrate"}:
        return copy_pack(args)
    if args.command == "validate":
        return validate_installation(args)
    return uninstall(args)


if __name__ == "__main__":
    raise SystemExit(main())
