from pathlib import Path
import ast
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "corinthians_dashboard.py"


class ProjectTests(unittest.TestCase):
    def test_script_has_valid_python_syntax(self) -> None:
        ast.parse(SCRIPT.read_text(encoding="utf-8"))

    def test_dashboard_discloses_sample_limit(self) -> None:
        source = SCRIPT.read_text(encoding="utf-8")
        self.assertIn("Illustrative, manually compiled dataset", source)
        self.assertNotIn("0.004%", source)

    def test_headless_backend_and_configurable_output(self) -> None:
        source = SCRIPT.read_text(encoding="utf-8")
        self.assertIn("matplotlib.use('Agg')", source)
        self.assertIn("--output", source)
        self.assertNotIn("plt.show()", source)

    def test_readme_does_not_present_sample_as_official(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("do not have row-level citations", readme)
        self.assertIn("official CBF reports", readme)


if __name__ == "__main__":
    unittest.main()
