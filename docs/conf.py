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
DISPLAY_VERSION = "0.12.7"


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
cwd = os.getcwd()
parent = os.path.dirname(cwd)
sys.path.insert(0, os.path.abspath(parent))

extensions = [
    'sphinx.ext.todo',
]

builddir = os.path.join(cwd, '_build')

# -- General configuration -----------------------------------------------------

linkcheck_ignore = [
    'https://groups.google.com/a/learningequality.org/forum/#!forum/dev',
    'http://127.0.0.1:8080',
    'http://127.0.0.1:8080/',
    'https://www.kiwix.org',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Where to find translated image files
figure_language_filename = '{path}{language}/{basename}{ext}'

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
