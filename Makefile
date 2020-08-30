init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock
	pipenv run pre-commit install
