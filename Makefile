
install:
	pipenv install --dev

clean:
	pipenv clean

shell:
	pipenv shell

dev:
	pipenv run uvicorn main:app --reload

check:
	black --check .

format:
	black .

.PHONY: install clean shell dev check format
