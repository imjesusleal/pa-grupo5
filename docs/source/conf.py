import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "tpo_grupo5"
copyright = (
    "2024, Sofia Arias Leal Jesus Paracare Jesus Benjumea Abraham Perez Leobaldo"
)
author = "Sofia Arias Leal Jesus Paracare Jesus Benjumea Abraham Perez Leobaldo"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme",
]

autodoc_member_order = "bysource"
autodoc_docstring_signature = True
autodoc_typehints = "description"

autodoc_default_options = {
    "members": True,
    "show-inheritance": True,
}
autosummary_generate = True

templates_path = ["_templates"]
exclude_patterns = []

language = "es"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
