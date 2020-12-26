
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

This is the user documentation repository of Kolibri, where documentation is maintained. The docs themselves are hosted at [kolibri.readthedocs.io](https://kolibri.readthedocs.io/).

To help translate the documentation, please visit our `'kolibri-docs' CrowdIn project <http://crowdin.com/project/kolibri-docs/>`__


Building the docs locally
-------------------------

You will need an environment with `make <https://en.wikipedia.org/wiki/Make_(software)>`__

.. code-block:: bash

  # Create a Python 3 virtual environment using Virtualenvwrapper
  # See: https://virtualenvwrapper.readthedocs.io/
  mkvirtualenv -p python3 kolibri-docs

  # Install Python requirements
  pip install -r requirements.txt


Build and run:

.. code-block:: bash

  make docs

You should now be able open the built docs with a web browser at ``docs/_build/html/index.html``.

You can also have the docs automatically build and reload:

.. code-block:: bash

  sphinx-autobuild docs docs/_build/html


You should now be able open the automatically-rebuilding docs with a web browser at ``http://127.0.0.1:8000``.


Internationalization
--------------------

Some commands related to i18n:

.. code-block:: bash

  # Build a translated (Spanish) version
  $ make docs-translated lang=es

  # Install the crowdin-cli client to download/upload translations
  $ make crowdin-install

  # Fetch translations
  $ CROWDIN_API_KEY="your-secret-key" make crowdin-download crowdin-branch=release-v0.7.x




Release process
---------------

When a new release of Kolibri happens, we track that release in a branch here with the
exact same name. We build this branch on Read The Docs.

* Changes to the **ENGLISH** documentation are accepted through Pull Requests here.
* Changes to other languages should happen on CrowdIn

When a new release happens and the English documentation is finalized, the source messages
for translation are uploaded to CrowdIn.

The languages (you're always welcome to request a new one!) are then worked out by translators
and approved. Once a language is improved sufficiently, we can fetch the latest strings from
CrowdIn and open up a new Pull Request here for the appropriate branch.

