# fastApiCleanArchitecture

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://docs.python.org/3/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![OpenAPI](https://img.shields.io/badge/openapi-6BA539?style=for-the-badge&logo=openapi-initiative&logoColor=fff)](https://www.openapis.org/)
[![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)](https://swagger.io/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://black.readthedocs.io/en/stable/)
[![Code test: pytest](https://img.shields.io/badge/code%20test-pytest-3670A0.svg?style=for-the-badge)](https://docs.pytest.org/en/7.4.x/)
[![Open Issues](https://img.shields.io/github/issues-raw/Felipe-Baz/fastapi-clean-architecture?style=for-the-badge)](https://github.com/Felipe-Baz/fastapi-clean-architecture/issues)
[![Closed Issues](https://img.shields.io/github/issues-closed-raw/Felipe-Baz/fastapi-clean-architecture?style=for-the-badge)](https://github.com/Felipe-Baz/fastapi-clean-architecture/issues?q=is%3Aissue+is%3Aclosed)
[![Open Pulls](https://img.shields.io/github/issues-pr-raw/Felipe-Baz/fastapi-clean-architecture?style=for-the-badge)](https://github.com/Felipe-Baz/fastapi-clean-architecture/pulls)
[![Closed Pulls](https://img.shields.io/github/issues-pr-closed-raw/Felipe-Baz/fastapi-clean-architecture?style=for-the-badge)](https://github.com/Felipe-Baz/fastapi-clean-architecture/pulls?q=is%3Apr+is%3Aclosed)
[![Contributors](https://img.shields.io/github/contributors/Felipe-Baz/fastapi-clean-architecture?style=for-the-badge)](https://github.com/Felipe-Baz/fastapi-clean-architecture/graphs/contributors)
[![Activity](https://img.shields.io/github/last-commit/Felipe-Baz/fastapi-clean-architecture?style=for-the-badge&label=most%20recent%20activity)](https://github.com/Felipe-Baz/fastapi-clean-architecture/pulse)

## Description

This is a project for study

## Installation

 - You can also open a shell inside virtual environment:

   ```sh
   make shell
   ```

 - Install all the project dependency using Pipenv:

   ```sh
   make install
   ```

 - Run the application from command prompt:

   ```sh
   make dev
   ```

 - Clean

   ```sh
   make clean
   ```

 - Open `localhost:8000/docs` for API Documentation

## Testing commands

 - Run tests:
   ```sh
   make tests
   ```

 - Run Coverage Report:

   ```sh
   make cov
   ```

## Format commands

 - Check the code style:

   ```sh
   make check
   ```

 - Format the code:

   ```sh
   make format
   ```

## Docker commands

 - Create `requirements.txt` with pipenv

   ```sh
   make requirements
   ```

 - Create a new docker image

   ```sh
   make docker_image
   ```

 - Run the API in a local container

   ```sh
   make docker_run
   ```

 - Deploy the docker image in docker hub

   ```sh
   make docker_push
   ```

## Kubernetes commands

 - Start kubernetes 

   ```sh
   make kube_start
   ```

 - Deploy changes of `kubernetes.yaml`

   ```sh
   make kube_deploy
   ```

 - Access the api in kubernetes

   ```sh
   make kube_access
   ```

 - Access kubernetes dashboard

   ```sh
   make kube_dash
   ```

## License

&copy; MIT License