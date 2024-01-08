"""Test API."""
from fastapi.testclient import TestClient

from {{ cookiecutter.project_package }}.api import app

client = TestClient(app)


def test_calculate():
    response = client.get("/calculate/divide?x=5&y=2")
    assert response.status_code == 200
    assert response.json() == 2  # int division

    response = client.get("/calculate/divide?x=5&y=0")
    assert response.status_code == 422
    assert "y=0" in response.json()["detail"]  # division by 0

    response = client.get("/calculate/add?x=3.14")
    assert response.status_code == 422  # float input

    response = client.get("/calculate/power?x=5")
    assert response.status_code == 422  # unsupported op
