## Lint using flake8, black, and isort (use `make format` to do formatting)
.PHONY: lint
lint:
	flake8 ./src ./tests
	isort --check --diff ./src ./tests
	black --check ./src ./tests
	mypy ./src ./tests
## Format source code with black
.PHONY: format
format: 
	isort ./src ./tests
	black ./src ./tests

## Run tests with pytest (use `make test`)
.PHONY: test
test:
	pytest tests

## Run streamlit app (use `make run`)
.PHONY: run
run:
	streamlit run src/frontend/ui.py
