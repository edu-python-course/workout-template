"""
Sphinx documentation generator configuration file

"""

import sys
from datetime import datetime
from pathlib import Path

# tomli package is included to the "docs" dependencies group
# noinspection PyPackageRequirements
import tomli

# set up
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR / "src"))

with open(BASE_DIR / "pyproject.toml", "rb") as io_buff:
    pyproject = tomli.load(io_buff)

copyright_opt = "Python training course authors and contributors"

# project information
# ===================
project = pyproject["tool"]["poetry"]["name"].replace("-", " ").title()
version = pyproject["tool"]["poetry"]["version"]
project_copyright = f"{datetime.now().year}, {copyright_opt}"
authors = " \\and ".join(pyproject["tool"]["poetry"]["authors"])

# general configuration
# =====================
master_doc = root_doc = "index"
extensions = [
    "sphinx.ext.autodoc",
    "myst_parser",

    "sphinx_immaterial",
]

source_suffix = {
    ".txt": "restructuredtext",
    ".rst": "restructuredtext",
    ".md": "markdown",
}
needs_sphinx = "4.0"
add_module_names = False

# options for internationalization
# ================================
gettext_compact = True
language = "en"
locale_dirs = ["_locales"]
gettext_allow_fuzzy_translations = True

# options for HTML output
# =======================
html_theme = "sphinx_immaterial"
html_favicon = "_static/favicon.ico"
html_theme_options = {
    # internationalization
    "languages": [
        {
            "name": "English",
            "link": "../en/",
            "lang": "en",
        },
        {
            "name": "Ukrainian",
            "link": "../uk",
            "lang": "uk",
        },
    ]
}
