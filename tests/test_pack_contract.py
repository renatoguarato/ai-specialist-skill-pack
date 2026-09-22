import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PackContractTests(unittest.TestCase):
    def test_representative_scenarios_use_v5_routes(self):
        scenarios = (ROOT / "evals/representative-scenarios.md").read_text(encoding="utf-8")
        migration = (ROOT / "MIGRATION.md").read_text(encoding="utf-8")
        legacy_names = set(re.findall(r"^\| `([^`]+)` \|", migration, re.MULTILINE))
        scenario_names = set(re.findall(r"`([a-z0-9-]+)`", scenarios))

        self.assertFalse(legacy_names & scenario_names)

    def test_new_modes_are_declared_by_public_skills(self):
        repository_skill = (ROOT / "skills/repository-discovery/SKILL.md").read_text(encoding="utf-8")
        delivery_skill = (ROOT / "skills/product-delivery/SKILL.md").read_text(encoding="utf-8")
        reliability_skill = (ROOT / "skills/production-reliability/SKILL.md").read_text(encoding="utf-8")

        self.assertIn("onboarding", repository_skill)
        self.assertIn("system-design", delivery_skill)
        self.assertIn("capacity", reliability_skill)
