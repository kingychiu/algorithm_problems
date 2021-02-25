
lint:
	pylint src

test:
	coverage run --source src -m pytest
	coverage report -m

new_problem:
	rm -rf ./src/${PROBLEM_NAME}
	cp -r ./src/template ./src/${PROBLEM_NAME}
