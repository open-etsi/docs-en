
import sys
sys.path.insert(0, '..')
sys.path.insert(0, '.')

project = "%writefile cache/index.md"
copyright = ""
author = "The contributors"
release = "0.0.1"

extensions = ["recommonmark","sphinxcontrib.bibtex","sphinxcontrib.rsvgconverter","sphinx.ext.autodoc","sphinx.ext.viewcode"]

# Customize bibtext_reference_style: https://github.com/mcmtroffaes/sphinxcontrib-bibtex/blob/develop/doc/usage.rst
from dataclasses import dataclass, field
import sphinxcontrib.bibtex.plugin

from sphinxcontrib.bibtex.style.referencing import BracketStyle
from sphinxcontrib.bibtex.style.referencing.author_year \
    import AuthorYearReferenceStyle
def bracket_style() -> BracketStyle:
    return BracketStyle(
        left='(',
        right=')',
    )
@dataclass
class MyReferenceStyle(AuthorYearReferenceStyle):
    bracket_parenthetical: BracketStyle = field(default_factory=bracket_style)
    bracket_textual: BracketStyle = field(default_factory=bracket_style)
    bracket_author: BracketStyle = field(default_factory=bracket_style)
    bracket_label: BracketStyle = field(default_factory=bracket_style)
    bracket_year: BracketStyle = field(default_factory=bracket_style)
sphinxcontrib.bibtex.plugin.register_plugin(
    'sphinxcontrib.bibtex.style.referencing',
    'author_year_round', MyReferenceStyle)

# For original square brackets, just set bibtex_reference_style = 'author_year'
# If unspecified, citet output will be "Zhang et al. [Zhang et al. 2022]" instead of "Zhang et al. (2022)"
bibtex_reference_style = 'author_year_round'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
master_doc = 'index'
numfig = True
numfig_secnum_depth = 2
math_numfig = True
math_number_all = True

suppress_warnings = ['misc.highlighting_failure']
linkcheck_ignore = [r'.*localhost.*']
linkcheck_timeout = 5
linkcheck_workers = 20

autodoc_default_options = {
    'undoc-members': True,
    'show-inheritance': True,
}


html_theme = 'mxtheme'
html_theme_options = {
    'primary_color': 'blue',
    'accent_color': 'deep_orange',
    'header_links': [
        ('PDF', 'https://book.d2l.ai/d2l-book.pdf', True, 'fas fa-file-pdf'),('Github', 'https://github.com/d2l-ai/d2l-book', True, 'fab fa-github'),
    ],
    'show_footer': False
}
html_static_path = ['_static']

html_favicon = ''

html_logo = ''

latex_documents = [
    (master_doc, "d2lbook.tex", "%writefile cache/index.md",
     author, 'manual'),
]

rsvg_converter_args = ['-z', '0.8']
bibtex_bibfiles = [""]
latex_engine = 'xelatex' # for utf-8 supports
latex_show_pagerefs = True
latex_show_urls = 'footnote'

latex_logo = ''

latex_elements = {

'figure_align': 'H',

'pointsize': '11pt',
'preamble': r'''

% Page size
\setlength{\voffset}{-14mm}
\addtolength{\textheight}{16mm}

% Chapter title style
\usepackage{titlesec, blindtext, color}
\definecolor{gray75}{gray}{0.75}
\newcommand{\hsp}{\hspace{20pt}}
\titleformat{\chapter}[hang]{\Huge\bfseries}{\thechapter\hsp\textcolor{gray75}{|}\hsp}{0pt}{\Huge\bfseries}

% So some large pictures won't get the full page
\renewcommand{\floatpagefraction}{.8}

\setcounter{tocdepth}{1}
% Use natbib's citation style, e.g. (Li and Smola, 16)
\usepackage{natbib}
\protected\def\sphinxcite{\citep}





% Remove top header
\setlength{\headheight}{13.6pt}
\makeatletter
    \fancypagestyle{normal}{
        \fancyhf{}
        \fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
        \fancyfoot[LO]{{\py@HeaderFamily\nouppercase{\rightmark}}}
        \fancyfoot[RE]{{\py@HeaderFamily\nouppercase{\leftmark}}}
        \fancyhead[LE,RO]{{\py@HeaderFamily }}
     }
\makeatother
% Defines macros for code-blocks styling
\definecolor{d2lbookOutputCellBackgroundColor}{RGB}{255,255,255}
\definecolor{d2lbookOutputCellBorderColor}{rgb}{.85,.85,.85}
\def\diilbookstyleoutputcell
   {\sphinxcolorlet{VerbatimColor}{d2lbookOutputCellBackgroundColor}%
    \sphinxcolorlet{VerbatimBorderColor}{d2lbookOutputCellBorderColor}%
    \sphinxsetup{verbatimwithframe,verbatimborder=0.5pt}%
   }%
%
\definecolor{d2lbookInputCellBackgroundColor}{rgb}{.95,.95,.95}
\def\diilbookstyleinputcell
   {\sphinxcolorlet{VerbatimColor}{d2lbookInputCellBackgroundColor}%
    \sphinxsetup{verbatimwithframe=false,verbatimborder=0pt}%
   }%
% memo: as this mark-up uses macros not environments we have to reset all changed
%       settings at each input cell to not inherit those or previous output cell
% memo: Sphinx 5.1.0, 5.1.1 ignore verbatimwithframe Boolean, so for this
%       reason we added an extra verbatimborder=0pt above.

''',

'sphinxsetup': '''verbatimsep=2mm,
                  VerbatimColor={rgb}{.95,.95,.95},
                  VerbatimBorderColor={rgb}{.95,.95,.95},
                  pre_border-radius=3pt,
               ''',
}
# memo: Sphinx 5.1.0+ has a "feature" that if we don't set VerbatimColor to
# some value via the sphinxsetup key or via \sphinxsetup raw macro, it
# considers no colouring of background is required.  Above we by-passed usage
# of \sphinxsetup, because \sphinxcolorlet was more convenient.  So we set
# VerbatimColor in 'sphinxsetup' global key to work around that "feature".
# The exact same applies with VerbatimBorderColor: it has to be set at least
# once via 'sphinxsetup' or via \sphinxsetup raw macro else frame is black.
#
# memo: the Sphinx 5.1.0+ added pre_border-radius must be used in 'sphinxsetup'
# (it can be modified later via extra  raw \sphinxsetup)
# because at end of preamble Sphinx decides whether or not to load extra package
# for rendering boxes with rounded corners.  N.B.: pre_border-radius is
# unknown in Sphinx < 5.1.0 and will cause breakage.



def setup(app):
    # app.add_js_file('https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.0/clipboard.min.js')
    app.add_js_file('d2l.js')
    app.add_css_file('d2l.css')
    import mxtheme
    app.add_directive('card', mxtheme.CardDirective)
