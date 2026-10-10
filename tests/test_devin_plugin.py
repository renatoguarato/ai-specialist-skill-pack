import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class DevinPluginTests(unittest.TestCase):
    def test_manifest_versions_match(self):
        pack = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        plugin = json.loads((ROOT / ".devin-plugin/plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(pack["version"], "6.0.0")
        self.assertEqual(plugin["version"], pack["version"])
        self.assertEqual(plugin["name"], pack["name"])

    def test_all_skills_have_frontmatter_and_contract(self):
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        for name in manifest["skills"]:
            with self.subTest(name=name):
                path = ROOT / "skills" / name / "SKILL.md"
                content = path.read_text(encoding="utf-8")
                self.assertTrue(content.startswith("---\n"))
                self.assertIn(f"name: {name}", content)
                self.assertIn("description:", content)
                self.assertIn("references/operating-contract.md", content)

    def test_plugin_has_operational_documentation(self):
        for path in ("AGENTS.md", "DEVIN_CLI.md", "agents/README.md"):
            self.assertTrue((ROOT / path).is_file())
