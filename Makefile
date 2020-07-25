test:
	coverage run --source src -m pytest
	coverage report

lint:
	pylint src