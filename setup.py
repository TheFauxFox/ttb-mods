import venv
from pathlib import Path

venv.create(Path("./.venv"), symlinks=True, with_pip=True)
