from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.routes import products, users
from app.exceptions import register_exception_handlers

app = FastAPI(title="FastAPI Control Work", version="1.0")

# Регистрируем обработчики исключений
register_exception_handlers(app)

# Обработчик ошибок валидации Pydantic
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content=jsonable_encoder({
            "detail": exc.errors(),
            "error_code": "VALIDATION_ERROR"
        })
    )

# Подключаем роутеры
app.include_router(products.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "FastAPI приложение работает", "status": "ok"}

@app.get("/health")
def health():
    return {"status": "healthy"}