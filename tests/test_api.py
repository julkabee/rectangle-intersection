from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_successful_intersection():
    """Тест успешного пересечения через API"""
    response = client.post("/intersect",
                           json={"x": 500, "y": 200, "w": 600, "h": 400})
    assert response.status_code == 200
    assert response.json() == {"x": 500, "y": 200, "w": 500, "h": 300}


def test_no_intersection():
    """Тест отсутствия пересечения через API"""
    response = client.post("/intersect",
                           json={"x": 1001, "y": 0, "w": 100, "h": 100})
    assert response.status_code == 200
    assert response.json() is None


def test_invalid_input():
    """Тест некорректного ввода (отсутствует поле)"""
    response = client.post("/intersect", json={"x": 100, "y": 100, "w": 100})
    assert response.status_code == 422
    assert "detail" in response.json()


def test_negative_coordinates():
    """Тест с отрицательными координатами"""
    response = client.post(
        "/intersect", json={"x": -100, "y": -100, "w": 150, "h": 150}
    )
    assert response.status_code == 200
    assert response.json() == {"x": 0, "y": 0, "w": 50, "h": 50}
