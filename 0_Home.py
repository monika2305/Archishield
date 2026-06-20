from pathlib import Path
import runpy


ROOT_HOME = Path(__file__).resolve().parent.parent / "Home.py"
runpy.run_path(str(ROOT_HOME), run_name="__main__")