"""
This is conf.py

Notes
-----

Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html.

Project information
https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

"""


'''
Basic
'''
project = 'Pages<br>'
project_copyright = '2024, SF & AIU'
author = 'SF & AIU'
release = 'v0.0.1<br>'


'''
General configuration
https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
https://myst-parser.readthedocs.io/en/v0.15.1/sphinx/intro.html#install-a-new-sphinx-extension-and-use-its-functionality
'''
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax',
    'sphinx_design',
    'sphinxcontrib.mermaid',
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    'myst_parser',
    'sphinx_issues'
]

myst_enable_extensions = [
    'amsmath',
    'attrs_inline',
    'colon_fence',
    'deflist',
    'dollarmath',
    'fieldlist',
    'html_admonition',
    'html_image',
    'replacements',
    'smartquotes',
    'strikethrough',
    'substitution',
    'tasklist',
    'attrs_block'
]

myst_url_schemes = {
    "https": None,
    "project-issue-item": {
        "url": "https://github.com/orgs/prml-0004/projects/2/views/5?pane=issue&itemId={{path}}",
        "title": "ISSUE ITEM: #{{path}}",
        "classes": ["github"],
    },
    "project-issue": {
        "url": "https://github.com/prml-0004/pages/issues/{{path}}",
        "title": "ISSUE: #{{path}}",
        "classes": ["github"],
    }
}



'''
https://myst-parser.readthedocs.io/en/latest/configuration.html
'''
myst_heading_anchors = 4


'''
Sphinx Issues
'''
issues_default_group_project = 'prml-0004/pages'


'''
Mathematics
'''
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'
myst_dmath_double_inline = True


'''
Paths that contain templates, relative to this directory.
'''
templates_path = ['_templates']


'''
List of patterns, relative to source directory, that match files and
directories to ignore when looking for source files.
This pattern also affects html_static_path and html_extra_path.
'''
exclude_patterns = []


'''
Options for HTML output
https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
'style_nav_header_background': '#343131'
html_logo = "_static/logo.svg"
'''

html_theme = 'sphinx_book_theme'

html_static_path = ['_static']

html_css_files = ['https://unpkg.com/tabulator-tables/dist/css/tabulator.min.css',
                  'https://cdnjs.cloudflare.com/ajax/libs/flickity/3.0.0/flickity.min.css',
                  'https://cdnjs.cloudflare.com/ajax/libs/prism/9000.0.1/themes/prism.min.css',
                  'css/figures.css',
                  'css/generic.css']

html_js_files = ['https://code.jquery.com/jquery-3.7.0.min.js',
                 'https://viewer.diagrams.net/js/viewer-static.min.js',
                 'https://cdnjs.cloudflare.com/ajax/libs/flickity/3.0.0/flickity.pkgd.min.js',
                 'https://cdnjs.cloudflare.com/ajax/libs/prism/9000.0.1/prism.min.js']

html_theme_options = {
    'use_download_button': True,
    'use_fullscreen_button': True,
    'home_page_in_toc': False,
    'show_navbar_depth': 1,
    'max_navbar_depth': 4,
    'collapse_navbar': False,
    'toc_title': 'PAGES',
    'show_toc_level': 2,
    'sidebarwidth': 250
}
