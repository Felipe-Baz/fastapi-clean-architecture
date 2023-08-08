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


## Installation

 - Install all the project dependency using Pipenv:

    ```sh
    make install
    ```

 - Run the application from command prompt:

    ```sh
    make dev
    ```

 - You can also open a shell inside virtual environment:

    ```sh
    make shell
    ```

 - Open `localhost:8000/docs` for API Documentation

 - Open `localhost:8000/graphql` for GraphQL Documentation

_*Note:* In case you are not able to access `pipenv` from you `PATH` locations, replace all instances of `pipenv` with `python3 -m pipenv`._

## Testing

For Testing, `unittest` module is used for Test Suite and Assertion, whereas `pytest` is being used for Test Runner and Coverage Reporter.

 - Run the following command to initiate test:
    ```sh
    make tests
    ```

 - To include Coverage Reporting as well:

    ```sh
    make cov
    ```

## License

&copy; MIT License