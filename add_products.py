from database import SessionLocal
from models import Product

db = SessionLocal()

# Добавляем первый продукт
product1 = Product(title="Ноутбук", price=50000, count=10)
db.add(product1)

# Добавляем второй продукт
product2 = Product(title="Мышь", price=1500, count=50)
db.add(product2)

db.commit()
db.close()

print("✅ Добавлено 2 продукта в таблицу products")