.PHONY: help clean clean-pyc clean-build list test test-all coverage docs release sdist

help:
	@echo "Usage:"
	@echo ""
	@echo "make <command>"
	@echo ""
	@echo "Building"
	@echo "--------"
	@echo ""
	@echo "docs: generate documentation in docs/_build/html"
	@echo "docs-translated lang=<LC>: generate translated documentation, e.g. make docs-translated lang=es"
	@echo "clean: restores code tree to a clean state"
	@echo ""
	@echo "Development"
	@echo "-----------"
	@echo ""
	@echo "lint: check Python style with flake8"
	@echo ""
	@echo "Internationalization"
	@echo "--------------------"
	@echo ""
	@echo "gettext: updates source messages for docs"
	@echo "crowdin-install: fetch crowdin-cli"
	@echo "crowdin-upload: crowdin-branch=<id> uploads docs translation sources via CrowdIn"
	@echo "crowdin-download crowdin-branch=<id>: downloads docs translated languages via CrowdIn"

clean:
	$(MAKE) -C docs clean

lint:
	$(MAKE) -C docs linkcheck

docs: clean
	$(MAKE) -C docs html

gettext:
	$(MAKE) -C docs gettext
	cd docs && sphinx-intl update -p _build/locale -l en

docs-translated:
	$(MAKE) -C docs -e SPHINXOPTS="-D language='${lang}'" html

crowdin-install:
	@`[ -f crowdin-cli.jar ]` && echo "Found crowdin-cli.jar" || wget -O crowdin-cli.jar https://storage.googleapis.com/le-downloads/crowdin-cli/crowdin-cli.jar

crowdin-upload:
	java -jar crowdin-cli.jar -c crowdin.yaml upload sources -b ${crowdin-branch}

crowdin-download:
	java -jar crowdin-cli.jar -c crowdin.yaml download -b ${crowdin-branch}
