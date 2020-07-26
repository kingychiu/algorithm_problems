test:
	coverage run --source src -m pytest
	coverage report

lint:
	pylint src

new_problem:
	rm -rf ./src/${problem_name}
	cp -r ./src/template ./src/${problem_name}
