## Lint using flake8, black, and isort (use `make format` to do formatting)
.PHONY: lint
lint:
	flake8 ./src ./app.py ./tests
	isort --check --diff ./src ./app.py ./tests
	black --check ./src ./app.py ./tests
	mypy ./src ./app.py ./tests
## Format source code with black
.PHONY: format
format: 
	isort ./src ./app.py ./tests
	black ./src ./app.py ./tests

## Run tests with pytest (use `make test`)
.PHONY: test
test:
	pytest tests

.PHONY: run
run:
	streamlit run src/frontend/ui.py