.ONESHELL:

.PHONY: install

install: venv
	@echo Buidling project with $(shell python --version)
	. venv/Scripts/activate; pip install .

venv:
	@echo creating venv for project in $(shell pwd)
	python -m venv ./venv 

clean:
	rm -rf ./venv
	rm -rf ./__pycache__
	rm -f "*.pyc"