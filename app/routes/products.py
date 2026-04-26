from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.exceptions import CustomExceptionA, CustomExceptionB
from database import get_db
from models import Product

router = APIRouter(prefix="/products", tags=["Products"])

# Схема для создания продукта
class ProductCreateSchema(BaseModel):
    title: str
    price: float
    count: int

@router.get("/search/{product_id}")
def search_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise CustomExceptionB(detail=f"Товар с ID {product_id} отсутствует")
    return {"id": product.id, "title": product.title, "price": product.price, "count": product.count}

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreateSchema, db: Session = Depends(get_db)):
    new_product = Product(
        title=product.title,
        price=product.price,
        count=product.count,
        description=""
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"id": new_product.id, "title": new_product.title, "price": new_product.price, "count": new_product.count}