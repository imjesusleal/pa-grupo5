.PHONY: format
format:
	black .
	isort .
	flake8
	pre-commit run --all-files
