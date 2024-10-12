.PHONY: setup run clean

# Python interpreter
PYTHON := python3

# Virtual environment
VENV := venv
VENV_ACTIVATE := $(VENV)/bin/activate

# Main application file
MAIN := main.py

setup: $(VENV_ACTIVATE)
	@echo "Setup complete. Activate the virtual environment with 'source $(VENV_ACTIVATE)'"

$(VENV_ACTIVATE): requirements.txt
	$(PYTHON) -m venv $(VENV)
	. $(VENV_ACTIVATE) && pip install --upgrade pip wheel setuptools
	. $(VENV_ACTIVATE) && pip install --prefer-binary --no-build-isolation -r requirements.txt

run: $(VENV_ACTIVATE)
	. $(VENV_ACTIVATE) && $(PYTHON) $(MAIN)

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

.DEFAULT_GOAL := run
