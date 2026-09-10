import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "install.py"


class InstallerTests(unittest.TestCase):
    def run_installer(self, *args):
        return subprocess.run(
            [sys.executable, str(INSTALLER), *map(str, args)],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )

    def test_install_is_idempotent_and_preserves_existing_agents(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            agents = repo / "AGENTS.md"
            agents.write_text("# Regras do projeto\n", encoding="utf-8")

            first = self.run_installer(repo, "--with-config")
            second = self.run_installer(repo)

            self.assertEqual(first.returncode, 0, first.stderr + first.stdout)
            self.assertEqual(second.returncode, 0, second.stderr + second.stdout)
            self.assertIn("# Regras do projeto", agents.read_text(encoding="utf-8"))
            self.assertIn("ai-specialist-pack:start", agents.read_text(encoding="utf-8"))
            self.assertEqual(len(list((repo / ".agents/skills").glob("*/SKILL.md"))), 50)
            self.assertTrue((repo / ".ai-specialist-pack/config.example.json").is_file())
            self.assertEqual(self.run_installer("validate", repo).returncode, 0)

    def test_conflict_requires_force(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            target = repo / ".agents/skills/01-codebase-inventory/SKILL.md"
            target.parent.mkdir(parents=True)
            target.write_text("local edit\n", encoding="utf-8")

            result = self.run_installer(repo)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("--force", result.stdout)

    def test_dry_run_does_not_write(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            result = self.run_installer(repo, "--dry-run")

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse((repo / ".agents").exists())
            self.assertFalse((repo / "AGENTS.md").exists())

    def test_uninstall_preserves_modified_skill(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            self.assertEqual(self.run_installer(repo).returncode, 0)
            skill = repo / ".agents/skills/01-codebase-inventory/SKILL.md"
            skill.write_text("local edit\n", encoding="utf-8")

            result = self.run_installer("uninstall", repo, "--yes")

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(skill.exists())
            self.assertFalse((repo / ".agents/skills/02-architecture-mapper/SKILL.md").exists())

    def test_uninstall_keeps_optional_config(self):
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            self.assertEqual(self.run_installer(repo, "--with-config").returncode, 0)

            result = self.run_installer("uninstall", repo, "--yes")

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((repo / ".ai-specialist-pack/config.example.json").exists())


if __name__ == "__main__":
    unittest.main()
