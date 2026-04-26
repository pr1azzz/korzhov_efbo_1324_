import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_async_get_root():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"

@pytest.mark.asyncio
async def test_async_create_and_get_product():
    from faker import Faker
    fake = Faker()
    
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Создаём продукт
        product_data = {
            "title": fake.word(),
            "price": fake.random_int(min=100, max=10000),
            "count": fake.random_int(min=1, max=100)
        }
        create_response = await ac.post("/products/create", json=product_data)
        assert create_response.status_code == 201
        product_id = create_response.json()["id"]
        
        # Получаем продукт
        get_response = await ac.get(f"/products/search/{product_id}")
        assert get_response.status_code == 200
        assert get_response.json()["title"] == product_data["title"]

@pytest.mark.asyncio
async def test_async_nonexistent_product():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/products/search/99999")
        assert response.status_code == 404