init:
	pip install -r requirements.txt

test:
	pytest tests

# Description of .PHONY @ https://stackoverflow.com/questions/2145590/what-is-the-purpose-of-phony-in-a-makefile
.PHONY: init test