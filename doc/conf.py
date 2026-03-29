# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys


# sys.path.insert(0, os.path.abspath("../../"))
sys.path.insert(0, os.path.abspath("../"))
# sys.path.insert(0, os.path.abspath("../../"))
print("path:")
print(sys.path)


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Manuals'
copyright = '2026, Spinlaboratory Team'
author = 'Spinlaboratory Team'
release = '0.1'

# from datetime import datetime
# date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

# def make_rst_epilog(rst_epilog_list):
#     rst_epilog = ""

#     for var, value in rst_epilog_list:
#         my_string = ".. " + "|" + var + "| replace:: " + value + "\n"

#         rst_epilog += my_string

#     rst_epilog += "\n"

#     return rst_epilog


# rst_epilog = make_rst_epilog(rst_epilog_list)


# # Add links from linkList.rst
# with open("_static/linkList.rst") as f:
#     rst_epilog += f.read()





# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    # "analytics_id":                     "G-917JV2CKD7",  #  Provided by Google in your dashboard
    # 'analytics_anonymize_ip':           False,
    "prev_next_buttons_location": "bottom",
    # 'style_external_links':             False,
    # 'vcs_pageview_mode':                '',
    # 'style_nav_header_background':      'white',
    "logo_only": False,
    # TOC options
    "sticky_navigation": False,
    "collapse_navigation": True,
    "navigation_depth": 4,
    # 'includehidden':                    True,
    # 'titles_only':                      False
    "flyout_display": "hidden",
    "version_selector": True,
    "language_selector": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


def setup(app):
    app.add_css_file("css/rtdSpinLabTtheme.css")

