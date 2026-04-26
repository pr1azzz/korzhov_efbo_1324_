import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_get_nonexistent_product():
    response = client.get("/products/search/99999")
    assert response.status_code == 404
    assert response.json()["error_code"] == "CUSTOM_B"

def test_create_product():
    response = client.post("/products/create", json={
        "title": "Тестовый товар",
        "price": 1000,
        "count": 5
    })
    assert response.status_code == 201
    assert response.json()["title"] == "Тестовый товар"

def test_validate_user_success():
    response = client.post("/users/validate", json={
        "username": "testuser",
        "age": 20,
        "email": "test@example.com",
        "password": "password123",
        "phone": "123456789"
    })
    assert response.status_code == 200

def test_validate_user_invalid_age():
    response = client.post("/users/validate", json={
        "username": "testuser",
        "age": 16,
        "email": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 422