# -*- coding: utf-8 -*-
#
# Kolibri 'user docs' documentation build configuration file
#
# This file is execfile()d with the current directory set to its containing dir.


from datetime import datetime
import os
import sys


# IMPORTANT! KEEP THIS UPDATED TO REFLECT WHICH VERSION THESE DOCS ARE WRITTEN
# FOR! DO NOT LET THEM BE TARGETTED AT MORE THAN ONE MINOR SERIES!
# I.E.: 0.1.x -- important to add 'dev' suffix for docs targetting development
# series.
DISPLAY_VERSION = "0.12.0.dev"


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
cwd = os.getcwd()
parent = os.path.dirname(cwd)
sys.path.insert(0, os.path.abspath(parent))

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.autodoc',
    'rst2pdf.pdfbuilder',
]

builddir = os.path.join(cwd, '_build')

# -- General configuration -----------------------------------------------------

linkcheck_ignore = [
    'https://groups.google.com/a/learningequality.org/forum/#!forum/dev',
    'http://127.0.0.1:8080',
    'http://127.0.0.1:8080/',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Kolibri'
copyright = u'{year:d}, Learning Equality'.format(year=datetime.now().year)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = DISPLAY_VERSION
# The full version, including alpha/beta/rc tags.
release = DISPLAY_VERSION

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '**/_*.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'


if on_rtd:
    os.system("sphinx-apidoc --doc-project='Python Reference' -f -o . ../kolibri ../kolibri/test ../kolibri/deployment/ ../kolibri/dist/")

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = ['.', sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# This should be commented back in for wide tables
# See: https://github.com/rtfd/readthedocs.org/issues/2116
# and: https://github.com/rtfd/sphinx_rtd_theme/pull/432

# html_context = {
#     'css_files': [
#         '_static/theme_overrides.css',  # override wide tables in RTD theme
#     ],
# }

# Approach for custom stylesheet:
# adapted from: http://rackerlabs.github.io/docs-rackspace/tools/rtd-tables.html
# and https://github.com/altair-viz/altair/pull/418/files
# https://github.com/rtfd/sphinx_rtd_theme/issues/117
def setup(app):
    # Add our custom CSS overrides
   app.add_stylesheet('theme_overrides.css')


# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# Output file base name for HTML help builder.
htmlhelp_basename = 'kolibri-user'

rst_prolog = """
.. role:: raw-html(raw)
      :format: html

.. |info| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">perm_device_information</span><span class="visuallyhidden">Info</span>`
.. |permissions| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">https</span><span class="visuallyhidden">Permissions</span>`
.. |edit| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">create</span><span class="visuallyhidden">Edit</span>`
.. |lock| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">https</span><span class="visuallyhidden">Permissions</span>`
.. |pencil| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">create</span><span class="visuallyhidden">Edit</span>`
.. |arrow-right| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">arrow_forward</span><span class="visuallyhidden">See next</span>`
.. |arrow-left| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">arrow_back</span><span class="visuallyhidden">See previous</span>`
.. |arrow-up| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">keyboard_arrow_up</span><span class="visuallyhidden">Arrow up</span>`
.. |arrow-down| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">keyboard_arrow_down</span><span class="visuallyhidden">Arrow down</span>`
.. |unlisted-channel| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">lock_open</span><span class="visuallyhidden">Unlisted channel</span>`
.. |lessons| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">import_contacts</span><span class="visuallyhidden">Lessons</span>`
.. |learners| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">people</span><span class="visuallyhidden">Learners</span>`
.. |users| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">people</span><span class="visuallyhidden">Users</span>`
.. |groups| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">group_work</span><span class="visuallyhidden">Groups</span>`
.. |recent| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">access_time</span><span class="visuallyhidden">Recent</span>`
.. |exams| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">assignment_late</span><span class="visuallyhidden">Quizzes</span>`
.. |channels| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">apps</span><span class="visuallyhidden">Channels</span>`
.. |settings| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">settings</span><span class="visuallyhidden">Settings</span>`
.. |data| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">save</span><span class="visuallyhidden">Data</span>`
.. |classes| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">domain</span><span class="visuallyhidden">Classes</span>`
.. |coach-resource| replace:: :raw-html:`<span class="material-icons local_library" aria-hidden="true">local_library</span><span class="visuallyhidden">Coach resource</span>`
.. |search| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">search</span><span class="visuallyhidden">Start search</span>`
.. |in-progress| replace:: :raw-html:`<span class="material-icons schedule" aria-hidden="true">schedule</span><span class="visuallyhidden">In progress</span>`
.. |started| replace:: :raw-html:`<span class="material-icons clock" aria-hidden="true">schedule</span><span class="visuallyhidden">Started</span>`
.. |completed| replace:: :raw-html:`<span class="material-icons star" aria-hidden="true">star</span><span class="visuallyhidden">Completed</span>`
.. |completed-small| replace:: :raw-html:`<span class="material-icons star-small" aria-hidden="true">stars</span><span class="visuallyhidden">Completed</span>`
.. |need-help| replace:: :raw-html:`<span class="material-icons help" aria-hidden="true">error</span><span class="visuallyhidden">Need help</span>`
.. |recommended| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">forum</span><span class="visuallyhidden">Recommended</span>`
.. |toc| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">list</span><span class="visuallyhidden">Table of content</span>`
.. |epub-settings| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">tune</span><span class="visuallyhidden">Ebook settings</span>`
.. |fullscreen| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">fullscreen</span><span class="visuallyhidden">Enter fullscreen</span>`
.. |previous-page| replace:: :raw-html:`<span class="material-icons outline" aria-hidden="true">keyboard_arrow_left</span><span class="visuallyhidden">Previous page</span>`
.. |next-page| replace:: :raw-html:`<span class="material-icons outline" aria-hidden="true">keyboard_arrow_right</span><span class="visuallyhidden">Next page</span>`
.. |class-home| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">dashboard</span><span class="visuallyhidden">Class home</span>`
.. |reports| replace:: :raw-html:`<span class="material-icons" aria-hidden="true">assessment</span><span class="visuallyhidden">Reports</span>`
.. |drag| replace:: :raw-html:`<span class="material-icons drag" aria-hidden="true">drag_indicator</span>`
.. |on-device| image:: img/on-device.png
   :alt: On your device
.. |green-check| image:: /img/on-device.png
   :alt: Correct answer
.. |topic-icon| image:: /img/topic-icon.png
   :alt: Topic
.. |video-icon| image:: /img/video-icon.png
   :alt: Video
.. |doc-icon| image:: /img/doc-icon.png
   :alt: Document
.. |exercise-icon| image:: /img/exercise-icon.png
   :alt: Exercise
.. |html-icon| image:: /img/html-icon.png
   :alt: App

"""

# Apr 5th: directive to allow .gif use for HTML docs with .png fallback for latexpdf
from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.supported_image_types = [
    'image/svg+xml',
    'image/gif',
    'image/png',
    'image/jpeg'
]



# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'kolibri', u'Kolibri Documentation',
     [u'Learning Equality'], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- I18N ----------------------------------------------------------------------

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

locale_dirs = [
    os.path.join(os.getcwd(), "locale", "docs"),
]


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

'fncychap': '\\usepackage{fncychap}',
    'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',

    'figure_align':'htbp',
    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '12pt',
    'extraclassoptions': 'oneside',
# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
'preamble': r'''
        %%%%%%%%%%%%%%%%%%%% Meher %%%%%%%%%%%%%%%%%%
        %%%add number to subsubsection 2=subsection, 3=subsubsection
        %%% below subsubsection is not good idea.
        \setcounter{secnumdepth}{3}
        %
        %%%% Table of content upto 2=subsection, 3=subsubsection
        \setcounter{tocdepth}{2}

        \usepackage{amsmath,amsfonts,amssymb,amsthm}
        \usepackage{graphicx}

        %%% reduce spaces for Table of contents, figures and tables
        %%% it is used "\addtocontents{toc}{\vskip -1.2cm}" etc. in the document
        \usepackage[notlot,nottoc,notlof]{}

        \usepackage{color}
        \usepackage{transparent}
        \usepackage{eso-pic}
        \usepackage{lipsum}

        \usepackage{footnotebackref} %%link at the footnote to go to the place of footnote in the text

        %% spacing between line
        \usepackage{setspace}
        \onehalfspacing
        % \doublespacing
        % \singlespacing


        %%%%%%%%%%% datetime
        \usepackage{datetime}

        \newdateformat{MonthYearFormat}{%
            \monthname[\THEMONTH], \THEYEAR}


        %% RO, LE will not work for 'oneside' layout.
        %% Change oneside to twoside in document class
        \usepackage{fancyhdr}
        \pagestyle{fancy}
        \fancyhf{}

        %%% Alternating Header for oneside
        \fancyhead[L]{\ifthenelse{\isodd{\value{page}}}{ \small \nouppercase{\leftmark} }{}}
        \fancyhead[R]{\ifthenelse{\isodd{\value{page}}}{}{ \small \nouppercase{\rightmark} }}

        %%% Alternating Header for two side
        %\fancyhead[RO]{\small \nouppercase{\rightmark}}
        %\fancyhead[LE]{\small \nouppercase{\leftmark}}

        %% for oneside: change footer at right side. If you want to use Left and right then use same as header defined above.
        \fancyfoot[R]{\ifthenelse{\isodd{\value{page}}}{{\tiny Learning Equality} }{\href{https://learningequality.org}{\tiny learningequality.org}}}

        %%% Alternating Footer for two side
        %\fancyfoot[RO, RE]{\scriptsize Learning Equality (info@learningequality.org)}

        %%% page number
        \fancyfoot[CO, CE]{\thepage}

        \renewcommand{\headrulewidth}{0.5pt}
        \renewcommand{\footrulewidth}{0.5pt}

        \RequirePackage{tocbibind} %%% comment this to remove page number for following
        \addto\captionsenglish{\renewcommand{\contentsname}{Table of contents}}
        \addto\captionsenglish{\renewcommand{\listfigurename}{List of figures}}
        \addto\captionsenglish{\renewcommand{\listtablename}{List of tables}}
        \addto\captionsenglish{\renewcommand{\listtablename}{List of tables}} %%% Heading for TOC


        %%reduce spacing for itemize
        \usepackage{enumitem}
        \setlist{nosep}

        %%%%%%%%%%% Quote Styles at the top of chapter
        \usepackage{epigraph}
        \setlength{\epigraphwidth}{0.8\columnwidth}
        \newcommand{\chapterquote}[2]{\epigraphhead[60]{\epigraph{\textit{#1}}{\textbf {\textit{--#2}}}}}
        %%%%%%%%%%% Quote for all places except Chapter
        \newcommand{\sectionquote}[2]{{\quote{\textit{``#1''}}{\textbf {\textit{--#2}}}}}
    ''',


    'maketitle': r'''
        \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1

        \begin{titlepage}
            \centering

            \vspace*{80mm} %%% * is used to give space from top
            \begin{figure}[!h]
            \centering
            \includegraphics[scale=0.75]{logo.png}
            \end{figure}
            
            \vspace{0mm}
            \textbf{\Huge {Kolibri User Guide}}

            \vspace{0mm}
            \small Published by Learning Equality


            %% \vfill adds at the bottom
            \vfill
            \small \textit{More information available at }{\href{https://learningequality.org}{learningequality.org}}
        \end{titlepage}

        \clearpage
        \pagenumbering{roman}
        \tableofcontents
        % \listoffigures
        % \listoftables
        \clearpage
        \pagenumbering{arabic}

        ''',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'sphinxsetup': \
        'hmargin={0.7in,0.7in}, vmargin={1in,1in}, \
        verbatimwithframe=true, \
        TitleColor={rgb}{0,0,0}, \
        HeaderFamily=\\rmfamily\\bfseries, \
        InnerLinkColor={rgb}{0,0,1}, \
        OuterLinkColor={rgb}{0,0,1}',

        'tableofcontents':' ',
}


# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'kolibri.tex', u'Kolibri User Guide',
   u'Published by learningequality.org', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None
latex_logo = 'logo.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# -- Options for PDF output --------------------------------------------------

# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author, options).
#
# If there is more than one author, separate them with \\.
# For example: r'Guido van Rossum\\Fred L. Drake, Jr., editor'
#
# The options element is a dictionary that lets you override
# this config per-document.
# For example,
# ('index', u'MyProject', u'My Project', u'Author Name',
#  dict(pdf_compressed = True))
# would mean that specific document would be compressed
# regardless of the global pdf_compressed setting.

pdf_documents = [
    ('index', u'Kolibri', u'Kolibri2', u'Learning Equality'),
]

# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['sphinx','kerning','a4']

# A list of folders to search for stylesheets. Example:
pdf_style_path = ['.', '_styles']

# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
pdf_compressed = False

# A colon-separated list of folders to search for fonts. Example:
pdf_font_path = ['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']

# Language to be used for hyphenation support
pdf_language = "en_US"

# Mode for literal blocks wider than the frame. Can be
# overflow, shrink or truncate
pdf_fit_mode = "shrink"

# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled
#pdf_break_level = 0

# When a section starts in a new page, force it to be 'even', 'odd',
# or just use 'any'
#pdf_breakside = 'any'

# Insert footnotes where they are defined instead of
# at the end.
#pdf_inline_footnotes = True

# verbosity level. 0 1 or 2
#pdf_verbosity = 0

# If false, no index is generated.
pdf_use_index = True

# If false, no modindex is generated.
#pdf_use_modindex = True

# If false, no coverpage is generated.
#pdf_use_coverpage = True

# Name of the cover page template to use
#pdf_cover_template = 'sphinxcover.tmpl'

# Documents to append as an appendix to all manuals.
#pdf_appendices = []

# Enable experimental feature to split table cells. Use it
# if you get "DelayedTable too big" errors
pdf_splittables = False

# Set the default DPI for images
#pdf_default_dpi = 72

# Enable rst2pdf extension modules (default is only vectorpdf)
# you need vectorpdf if you want to use sphinx's graphviz support
#pdf_extensions = ['vectorpdf']

# Page template name for "regular" pages
#pdf_page_template = 'cutePage'

# Show Table Of Contents at the beginning?
#pdf_use_toc = True

# How many levels deep should the table of contents be?
#pdf_toc_depth = 3

# Add section number to section references
pdf_use_numbered_links = False

# Background images fitting mode
pdf_fit_background_mode = 'scale'

# Repeat table header on tables that cross a page boundary?
pdf_repeat_table_rows = True 

