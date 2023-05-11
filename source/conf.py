# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from docutils import nodes
from docutils.parsers.rst import Directive

# -- Project information -----------------------------------------------------

project = 'ML Notes'
copyright = '2022, ZHANG, Meng'
author = 'ZHANG, Meng'


class DisqusDirective(Directive):
    has_content = False
    required_arguments = 0
    optional_arguments = 0

    def run(self):
        docname = self.state.document.settings.env.docname
        disqus_node = nodes.raw(
            '',
            '<div id="disqus_thread" data-identifier="%s"></div>' % docname,
            format='html')
        return [disqus_node]


def setup(app):
    app.add_directive('disqus', DisqusDirective)


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.mathjax',
    'sphinxcontrib.bibtex',
]
bibtex_bibfiles = ["refs.bib"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = "piccolo_theme"
html_title = "Machine Learning Notes"
html_short_title = "ML Notes"
# Set the logo
# html_logo = "_static/logo.png"
# Set the favicon
# html_favicon = "_static/favicon.ico"
# Set the color palette
html_theme_options = {
    "source_url": "https://github.com/ppmzhang2/ppmzhang2.github.io",
    "source_icon": "github",
    # "banner_text": "Explore Machine Learning - One Note at a Time",
    # "banner_hiding": "temporary",
}
pygments_style = "friendly"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_js_files = [
    "js/disqus.js",
]
