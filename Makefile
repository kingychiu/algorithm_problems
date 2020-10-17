# Commands running inside k8s:
k8s-test:
	coverage run --source src -m pytest
	coverage report -m

k8s-lint:
	pylint src

# Commands for development
cleanup:
	skaffold delete -f "skaffold/linter.yaml"
	skaffold delete -f "skaffold/tester.yaml"

lint:
	skaffold run -f "skaffold/linter.yaml" --tail

test:
	skaffold run -f "skaffold/tester.yaml" --tail

new_problem:
	rm -rf ./src/${problem_name}
	cp -r ./src/template ./src/${problem_name}
