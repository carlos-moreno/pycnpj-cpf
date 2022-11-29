.PHONY: virtualenv install ipython lint fmt test watch clean docs docs-serve build publish-test publish

virtualenv:
	@python -m venv .venv

install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

ipython:
	@.venv/bin/ipython

lint:
	@.venv/bin/pflake8

fmt:
	@.venv/bin/isort core tests
	@.venv/bin/black core tests

test:
	@.venv/bin/pytest -s

watch:
	@ls **/*.py | entr pytest

clean: ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build

docs:
	@mkdocs build --clean

docs-serve:
	@mkdocs serve

build:
	@python setup.py sdist bdist_wheel

publish-test:
	@twine upload --repository testpypi dist/*

publish:
	@twine upload dist/*
