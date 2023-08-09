
install:
	pipenv install --dev

clean:
	pipenv clean

shell:
	pipenv shell

dev:
	pipenv run uvicorn app.main:app --reload

check:
	black --check .

format:
	black .

tests:
	pipenv run pytest

cov:
	pipenv run pytest --cov-report=html --cov .

docker_image:
	docker build -t fastapi_image .

docker_run:
	docker run -d --name fastapi_container -p 5000:5000 fastapi_image

requirement:
	pipenv requirement > requirement.txt

.PHONY: install clean shell dev check format tests cov docker_image docker_run
