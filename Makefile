
lint:
	poetry run pylint src

type-check:
	poetry run mypy src

test:
	poetry run coverage run --source src -m pytest
	poetry run coverage report -m

new_problem:
	rm -rf ./src/${PROBLEM_NAME}
	cp -r ./src/template ./src/${PROBLEM_NAME}
