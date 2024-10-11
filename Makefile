.PHONY: format
format:
	black .
	isort .
	flake8
	pre-commit run --all-files

.PHONY:build
build:
	python -m build
	pip install -e .
