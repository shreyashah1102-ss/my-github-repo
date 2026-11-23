import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryBasicsTests(unittest.TestCase):
    def test_readme_exists_is_readable_and_not_empty(self):
        readme = ROOT / "README.md"

        self.assertTrue(readme.is_file())
        text = readme.read_text(encoding="utf-8")
        self.assertGreater(len(text.strip()), 0)

    def test_readme_has_project_title(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("# my-github-repo", readme)

    def test_git_attributes_marks_generated_workflows(self):
        attributes = ROOT / ".gitattributes"

        self.assertTrue(attributes.is_file())
        text = attributes.read_text(encoding="utf-8")
        self.assertIn(".github/workflows/*.lock.yml linguist-generated=true", text)

    def test_test_workflow_exists_with_main_triggers(self):
        workflow = ROOT / ".github" / "workflows" / "tests.yml"

        self.assertTrue(workflow.is_file())
        text = workflow.read_text(encoding="utf-8")

        self.assertIn("push:", text)
        self.assertIn("pull_request:", text)
        self.assertIn("branches: [main]", text)

    def test_test_workflow_runs_unittest_suite(self):
        workflow = (
            ROOT / ".github" / "workflows" / "tests.yml"
        ).read_text(encoding="utf-8")

        self.assertIn("python3 -m unittest discover -s tests -v", workflow)


if __name__ == "__main__":
    unittest.main()
