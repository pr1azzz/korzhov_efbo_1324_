from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

class CustomExceptionA(HTTPException):
    def __init__(self, detail: str = "Ошибка A: Неверный запрос"):
        super().__init__(status_code=400, detail=detail)

class CustomExceptionB(HTTPException):
    def __init__(self, detail: str = "Ошибка B: Ресурс не найден"):
        super().__init__(status_code=404, detail=detail)

def register_exception_handlers(app):
    @app.exception_handler(CustomExceptionA)
    async def custom_a_handler(request: Request, exc: CustomExceptionA):
        return JSONResponse(
            status_code=exc.status_code,
            content=jsonable_encoder({
                "error": exc.detail,
                "error_code": "CUSTOM_A",
                "status": exc.status_code
            })
        )
    
    @app.exception_handler(CustomExceptionB)
    async def custom_b_handler(request: Request, exc: CustomExceptionB):
        return JSONResponse(
            status_code=exc.status_code,
            content=jsonable_encoder({
                "error": exc.detail,
                "error_code": "CUSTOM_B",
                "status": exc.status_code
            })
        )