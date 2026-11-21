"""Offline Git semantics tests; temporary fixture repositories only."""
import subprocess
import tempfile
import unittest
from pathlib import Path


def git(folder, *args):
    return subprocess.run(['git', '-C', str(folder), *args], text=True,
                          capture_output=True, check=True).stdout.strip()

class LocalGitSemanticsTests(unittest.TestCase):
    def _fixture(self, directory):
        root=Path(directory)
        (root/'.gitignore').write_text('/.secrets/\n/secrets/\n.env\nLibrary/\n')
        (root/'README.md').write_text('Example\n')
        git(root,'init','-b','main')
        # Explicitly fictitious test fixture identity, never a real human or agent.
        git(root,'config','user.name','Fixture Author')
        git(root,'config','user.email','fixture-author@agents.invalid')
        git(root,'add','README.md','.gitignore')
        git(root,'commit','-m','test: initial fixture')
        return root

    def test_git_init_does_not_replace_existing_gitignore(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            expected='/.secrets/\n/secrets/\n.env\nLibrary/\n'
            (root/'.gitignore').write_text(expected)
            git(root,'init','-b','main')
            self.assertEqual((root/'.gitignore').read_text(), expected)
            (root/'secrets').mkdir()
            (root/'secrets'/'secret.txt').write_text('fixture-data')
            self.assertIn('secrets/secret.txt',git(root,'check-ignore','-v','secrets/secret.txt'))

    def test_non_squash_merge_preserves_source_commit_after_branch_deleted(self):
        with tempfile.TemporaryDirectory() as temp:
            root=self._fixture(temp)
            git(root,'branch','dev')
            git(root,'switch','dev')
            git(root,'switch','-c','feat/TASK-1-example')
            (root/'feature.txt').write_text('feature A\n')
            git(root,'add','feature.txt')
            git(root,'commit','-m','feat: example implementation')
            source_tip=git(root,'rev-parse','HEAD')
            git(root,'switch','dev')
            git(root,'merge','--no-ff','--no-edit','feat/TASK-1-example')
            merge_commit=git(root,'rev-parse','HEAD')
            self.assertEqual(len(git(root,'rev-list','--parents','-n','1',merge_commit).split()),3)
            git(root,'merge-base','--is-ancestor',source_tip,'dev')
            git(root,'branch','-d','feat/TASK-1-example')
            self.assertIn(source_tip,git(root,'rev-list','dev').splitlines())
            self.assertIn('main',git(root,'branch','--list','main'))

if __name__=='__main__':
    unittest.main()
