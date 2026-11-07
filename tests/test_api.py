from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_prediction():
    response = client.post(
        "/predict",
        json={"age": 30, "monthly_income": 80000}
    )

    assert response.status_code == 200
    assert response.json()["prediction"] == 1