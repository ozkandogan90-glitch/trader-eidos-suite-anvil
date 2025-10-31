.PHONY: help install dev test format lint type-check clean docs

help:
	@echo "Trader Eidos Suite - Development Commands"
	@echo "=========================================="
	@echo "make install          - Install dependencies"
	@echo "make dev              - Install dev dependencies"
	@echo "make test             - Run tests"
	@echo "make format           - Format code with black and isort"
	@echo "make lint             - Run linting (flake8, pylint)"
	@echo "make type-check       - Run type checking (mypy)"
	@echo "make clean            - Clean temporary files"
	@echo "make docs             - Build documentation"
	@echo "make pre-commit-init  - Setup pre-commit hooks"

install:
	pip install -r requirements.txt

dev: install
	pip install -r requirements-dev.txt

test:
	pytest tests/ -v --cov=server_code

format:
	black server_code/ client_code/
	isort server_code/ client_code/

lint:
	flake8 server_code/ client_code/
	pylint server_code/ client_code/

type-check:
	mypy server_code/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf build/ dist/

docs:
	cd docs && make html

pre-commit-init:
	pre-commit install
	pre-commit run --all-files

all: format lint type-check test

.DEFAULT_GOAL := help
