setup_check:
	@echo 'setup has started'
	pip install -r requirements.txt
	@echo 'check has started'
	mypy main.py
	flake8 --ignore=E501 main.py
	@echo 'test has started'
	pytest

run: setup_check
	python main.py

