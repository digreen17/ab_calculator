## Lint using flake8, black, and isort (use `make format` to do formatting)
.PHONY: lint
lint:
	flake8 ./src ./prob.py ./tests
	isort --check --diff ./src ./prob.py ./tests
	black --check ./src ./prob.py ./tests

## Format source code with black
.PHONY: format
format: 
	isort ./src ./prob.py ./tests
	black ./src ./prob.py ./tests

## Run tests with pytest (use `make test`)
.PHONY: test
test:
	pytest tests
