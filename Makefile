lint:
	flake8 web_parser

run_test:
	python -m unittest discover .

test_report:
	python -m unittest -vv tests.test_app