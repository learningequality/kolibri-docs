
Kolibri Docs
============

.. image:: https://api.travis-ci.org/learningequality/kolibri-docs.svg?branch=develop
  :target: https://travis-ci.org/learningequality/kolibri-docs
.. image:: https://img.shields.io/badge/docs-user-ff69b4.svg
  :target: http://kolibri.readthedocs.org/en/latest/
.. image:: https://img.shields.io/badge/translate-crowdin-69ffb4.svg
  :target: http://crowdin.com/project/kolibri-docs/
.. image:: https://img.shields.io/badge/support-on%20discourse-blue.svg
  :target: https://community.learningequality.org/
.. image:: https://img.shields.io/badge/demo-online-green.svg
  :target: http://kolibridemo.learningequality.org/


What is this?
-------------

This is the Documentation repository of Kolibri, where documentation is built.

To translate the documentation, please visit our `CrowdIn project kolibri-docs <http://crowdin.com/project/kolibri-docs/>`__


Building the docs locally
-------------------------

You will need an environment with `make <https://en.wikipedia.org/wiki/Make_(software)>`__

.. code-block:: bash

  # Create a Python 3 virtual environment using Virtualenvwrapper
  # See: https://virtualenvwrapper.readthedocs.io/
  $ mkvirtualenv -p python3 kolibri-docs

  # Install Python requirements
  $ pip install -r requirements.txt

  # Build docs with Sphinx
  $ make docs  

  # Open the docs with Firefox
  $ firefox docs/_build/html/index.html

  # Build a translated (Spanish) version
  $ make docs-translated lang=es

  # Install the crowdin-cli client to download/upload translations
  $ make crowdin-install

  # Fetch translations
  $ CROWDIN_API_KEY="your-secret-key" make crowdin-download crowdin-branch=release-v0.7.x


Workflow
--------

When a new release of Kolibri happens, we track that release in a branch here with the
exact same name. We build this branch on Read The Docs.

* Changes to the **ENGLISH** documentation are accepted through Pull Requests here.
* Changes to other languages should happen on CrowdIn

When a new release happens and the English documentation is finalized, the source messages
for translation are uploaded to CrowdIn.

The languages (you're always welcome to request a new one!) are then worked out by translators
and approved. Once a language is improved sufficiently, we can fetch the latest strings from
CrowdIn and open up a new Pull Request here for the appropriate branch.

