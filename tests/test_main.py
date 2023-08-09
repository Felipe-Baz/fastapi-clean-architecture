from fastapi.testclient import TestClient

from app.configs.Environment import get_environment_variables
from app.main import app

client = TestClient(app)
env = get_environment_variables()


def test_read_main():
    response = client.get("/v1/health")
    assert response.status_code == 200
    assert response.json() == {"version": env.API_VERSION}
