# docs/conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('../'))

project = 'Your Project Name'
copyright = '2025'
author = 'Your Name'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # For Google/NumPy docstring style
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
