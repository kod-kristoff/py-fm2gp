.PHONY: venv help test clean clean-pyc

.default: help

help:
	@echo "usage:"


ifeq (${VIRTUAL_ENV},)
  VENV_NAME = .venv
  VENV_BIN = ${VENV_NAME}/bin
  ${info Using ${VENV_NAME}}
else
  VENV_NAME = ${VIRTUAL_ENV}
  VENV_BIN = ${VENV_NAME}/bin
  ${info Using ${VENV_NAME}}
endif
ifeq (${VIRTUAL_ENV},)
  VENV_ACTIVATE = . ${VENV_BIN}/activate
else
  VENV_ACTIVATE = true
endif
PYTHON = ${VENV_BIN}/python


venv: ${VENV_NAME}/venv.created

${VENV_NAME}/venv.created:
	test -d ${VENV_NAME} || python -m venv ${VENV_NAME}
	@touch $@

${VENV_NAME}/dev.installed: setup.py setup.cfg requirements.txt
	${VENV_ACTIVATE}; python -m pip install -e .[dev]
	@touch $@

install-dev: venv ${VENV_NAME}/dev.installed

test: install-dev clean-pyc
	${VENV_ACTIVATE}; pytest -vv --cov=src  --cov-report=term tests

VERSION_PATCH = $(shell bumpversion --dry-run --list patch | grep new_version | sed -r s/'^.*='//)
VERSION_MINOR = $(shell bumpversion --dry-run --list minor | grep new_version | sed -r s/'^.*='//)
VERSION_MAJOR = $(shell bumpversion --dry-run --list major | grep new_version | sed -r s/'^.*='//)

bumpversion-patch:
	bumpversion patch
	${info version=${VERSION_PATCH}}
	git tag -a -m "Version ${VERSION_PATCH}" v${VERSION_PATCH}

bumpversion-minor:
	bumpversion minor
	${info version=${VERSION_MINOR}}
	git tag -a -m "Version ${VERSION_MINOR}" v${VERSION_MINOR}

bumpversion-major:
	bumpversion major
	${info version=${VERSION_MAJOR}}
	git tag -a -m "Version ${VERSION_MAJOR}" v${VERSION_MAJOR}

clean: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm {} \;
	# find src -type d -name '__pycache__' -exec rm -rf {} \;
	rm -rf .pytest_cache
