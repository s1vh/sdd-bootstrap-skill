"""Portable policy smoke tests for the experimental SDD Bootstrap Skill.

These assert presence/coherence of normative instructions, not that an AI agent
will obey them. No external services, accounts, secrets, or deployments used.
Run from repository root: python -m unittest discover -s tests -p 'test_sdd_bootstrap_v02.py' -v
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'sdd-bootstrap/SKILL.md'
CONTRACT = ROOT / 'sdd-bootstrap/references/PROJECT_CONVENTIONS.md'

class ExperimentalContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = SKILL.read_text(encoding='utf-8')
        cls.contract = CONTRACT.read_text(encoding='utf-8')

    def test_skill_metadata_and_entrypoint(self):
        self.assertTrue(self.skill.startswith('---\nname: sdd-bootstrap\n'))
        self.assertIn('## 15. Reference Library', self.skill)

    def test_no_git_initialization_as_default(self):
        self.assertIn('without an initialized `.git/` directory', self.skill)
        self.assertIn('no `.git/` directory', self.contract)
        self.assertNotIn('default convention requires an initialized Git repository', self.skill)

    def test_gitignore_survives_first_git_transition(self):
        for marker in ('`.gitignore`', '`/.secrets/`', '`/secrets/`', 'First-Git transition guard'):
            self.assertIn(marker, self.contract)
        self.assertIn('`git check-ignore -v`', self.contract)

    def test_identity_no_model_or_platform_guessing(self):
        for marker in ('**No inherited technical identity:**','current model', 'previous commits', 'Unknown fields are **omitted**'):
            self.assertIn(marker, self.contract)
        self.assertIn('`@ platform`', self.skill)

    def test_coauthor_trailers_and_approved_emails(self):
        self.assertIn('`Co-authored-by:', self.contract)
        self.assertIn('human owner\'s email requires the owner\'s explicit request', self.contract)
        self.assertIn('agents.invalid', self.contract)

    def test_no_default_squash_or_preserve_source_branch(self):
        self.assertIn('`git merge --no-ff`', self.contract)
        self.assertIn('`git branch -d`', self.contract)
        self.assertNotIn('**Default integration:** after suitable', self.contract)
        self.assertIn('Preserve original history reachable from `dev`', self.contract)

    def test_ordinary_dev_merges_are_agent_autonomous(self):
        self.assertIn('**without per-merge human confirmation**', self.contract)
        self.assertIn('completed no-squash topic→`dev` merge commits', self.contract)

    def test_main_remains_human_controlled(self):
        self.assertIn('specific authorization', self.contract)
        self.assertIn('ordinarily performs `dev`→`main` manually', self.contract)
        self.assertIn('Never deploy from `dev` or a topic branch', self.contract)
        self.assertIn('rebasing/history rewriting requires', self.contract)

    def test_cheap_vs_expensive_testing(self):
        self.assertIn('smallest relevant inexpensive checks', self.contract)
        self.assertIn('**Gameplay tests MUST run ONLY', self.contract)
        self.assertIn('explicit authorization from the human', self.contract)

    def test_pilot_horizon_and_hard_constraints(self):
        for marker in ('critical end-to-end', 'hard constraints', 'later commercial/scale', 'CPU time per invocation'):
            self.assertIn(marker, self.skill)

    def test_unverified_feasibility_not_claimed_as_proven(self):
        self.assertIn('A plan-tier quota or compatibility claim without a tested critical flow', self.skill)
        self.assertIn('If none meets hard constraints', self.contract)

    def test_default_no_git_is_implementation_ready_when_other_requirements_met(self):
        self.assertIn('no special exception', self.contract.lower())
        self.assertIn('not incomplete merely for lacking Git', self.skill)

    def test_no_mock_project_license_inheritance(self):
        self.assertIn('do not inherit this license', self.skill)

    def test_d11_through_d14_review_trackable(self):
        for decision in ('D11','D12','D13','D14'):
            self.assertRegex(self.contract, rf'\| {decision} \|')

if __name__ == '__main__':
    unittest.main()
