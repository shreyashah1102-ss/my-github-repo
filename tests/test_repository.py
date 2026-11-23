import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryBasicsTests(unittest.TestCase):
    def test_readme_exists_and_is_not_empty(self):
        readme = ROOT / "README.md"

        self.assertTrue(readme.is_file())
        self.assertGreater(len(readme.read_text(encoding="utf-8").strip()), 0)

    def test_readme_has_project_title(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("# my-github-repo", readme)

    def test_git_attributes_exists_and_is_readable(self):
        attributes = ROOT / ".gitattributes"

        self.assertTrue(attributes.is_file())
        self.assertIsInstance(attributes.read_text(encoding="utf-8"), str)

    def test_test_workflow_exists(self):
        workflow = ROOT / ".github" / "workflows" / "tests.yml"

        self.assertTrue(workflow.is_file())

    def test_test_workflow_runs_on_main_push_and_pull_request(self):
        workflow = (
            ROOT / ".github" / "workflows" / "tests.yml"
        ).read_text(encoding="utf-8")

        self.assertIn("push:", workflow)
        self.assertIn("pull_request:", workflow)
        self.assertIn("branches: [main]", workflow)
        self.assertIn("python3 -m unittest discover -s tests -v", workflow)


if __name__ == "__main__":
    unittest.main()
