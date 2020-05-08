# # Configuration file for the Sphinx documentation builder.
# #
# # This file only contains a selection of the most common options. For a full
# # list see the documentation:
# # https://www.sphinx-doc.org/en/master/usage/configuration.html


# def _get_version() -> str:
#     from pathlib import Path
#     from tomlkit import parse

#     pyproject_path = Path(__file__).resolve().parent.joinpath("../pyproject.toml")
#     with open(pyproject_path) as file:
#         pyproject = parse(file.read())

#     return str(pyproject["tool"]["poetry"]["version"])


# # -- Project information -----------------------------------------------------

# project = "pyrh"
# copyright = "2020, Unofficial Robinhood Python API"
# author = "Unofficial Robinhood Python API"
# master_doc = "index"
# exclude_patterns = ["stubs/*"]  # ignore stubs from checks

# # The full version, including alpha/beta/rc tags
# release = _get_version()

# # -- General configuration ---------------------------------------------------

# # Add any Sphinx extension module names here, as strings. They can be
# # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# # ones.
# extensions = [
#     "sphinx.ext.autodoc",
#     "sphinx.ext.napoleon",
#     "sphinx.ext.intersphinx",
#     "autodocsumm",
#     "sphinx_autodoc_typehints",
# ]

# # Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

# # List of patterns, relative to source directory, that match files and
# # directories to ignore when looking for source files.
# # This pattern also affects html_static_path and html_extra_path.
# exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# # -- Options for HTML output -------------------------------------------------

# # The theme to use for HTML and HTML Help pages.  See the documentation for
# # a list of builtin themes.
# #
# html_theme = "sphinx_rtd_theme"

# # Add any paths that contain custom static files (such as style sheets) here,
# # relative to this directory. They are copied after the builtin static files,
# # so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

# # source_suffix = '.rst'
# source_suffix = [".rst"]

# # intersphinx
# intersphinx_mapping = {
#     "requests": ("https://requests.readthedocs.io/en/master/", None),
# }

# # Autodoc
# autodoc_default_flags = ["members"]
# autosummary_generate = True
