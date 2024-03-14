"""
Sphinx documentation generator configuration file

"""

import sys
from datetime import datetime
from pathlib import Path

import toml

# set up
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "src"))

with open(BASE_DIR / "pyproject.toml") as io_buff:
    pyproject = toml.load(io_buff)

copyright_opt = "Python training course authors and contributors"

# project information
# ===================
project = pyproject["tool"]["poetry"]["name"]
version = pyproject["tool"]["poetry"]["version"]
project_copyright = f"{datetime.now().year}, {copyright_opt}"
authors = " \\and ".join(pyproject["tool"]["poetry"]["authors"])

# general configuration
# =====================
master_doc = root_doc = "index"
extensions = [
    "sphinx.ext.autodoc",
    "myst_parser",
]

source_suffix = {
    ".txt": "restructuredtext",
    ".rst": "restructuredtext",
    ".md": "markdown",
}
needs_sphinx = "4.0"
add_module_names = False

# options for internationalization
gettext_compact = False
language = "en"
locale_dirs = ["_locales"]
gettext_allow_fuzzy_translations = True

# options for HTML output
html_theme = "sphinx_material"
html_favicon = "_static/favicon.ico"
