.PHONY: virtualenv install ipython lint fmt test security watch clean docs docs-serve build publish-test publish

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
	@.venv/bin/isort pycnpj_cpf tests
	@.venv/bin/black pycnpj_cpf tests

test:
	@.venv/bin/pytest --cov=pycnpj_cpf --cov-report=xml -vv

security:
	@.venv/bin/bandit -c pyproject.toml -r .

watch:
	@ls **/*.py | entr pytest

clean:
	@find . -depth -maxdepth 5 -name '*.pyc' -exec rm -rf {} \;
	@find . -depth -maxdepth 5 -name '__pycache__' -exec rm -rf {} \;
	@find . -depth -maxdepth 5 -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -depth -maxdepth 5 -name '*~' -exec rm -rf {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build
	@rm -rf .coverage
	@rm -rf coverage.xml


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
