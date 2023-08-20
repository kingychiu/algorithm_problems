
lint:
	poetry run isort --profile black ./src
	poetry run black ./src
	poetry run ruff check ./src
	poetry run mypy ./src

test:
	poetry run pytest -s --cov=src \
	--no-cov-on-fail --cov-fail-under=100 --cov-report=term-missing:skip-covered \
	$(PATH)

test_all:
	make test PATH=src

timed_test:
	poetry run pytest -s -vv --durations=0 $(PATH)

timed_test_all:
	make timed_test PATH=src

new_problem:
	rm -rf ./src/${PROBLEM_NAME}
	cp -r ./src/template ./src/${PROBLEM_NAME}
