bold := $(shell tput bold)
sgr0 := $(shell tput sgr0)

init: venv/pyenv.cfg
	@printf "${bold}Buidling project with $(shell python --version)${sgr0}\n"
	. venv/Scripts/activate; pip install .

venv/pyenv.cfg: venv

venv:
	@printf "${bold}Creating venv for project in $(shell pwd)${sgr0}\n"
	python -m venv ./venv 

clean:
	@printf "${bold}Removing /venv directory and __pycache__ files${sgr0}\n"
	@rm -rf ./venv
	@rm -rf ./__pycache__
	@rm -f "*.pyc"