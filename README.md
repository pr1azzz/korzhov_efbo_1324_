# Контрольная работа №4

## Описание проекта
FastAPI приложение с поддержкой:
- Миграции базы данных (Alembic + PostgreSQL)
- Пользовательские исключения и обработка ошибок
- Валидация данных (Pydantic)
- Модульные и асинхронные тесты (pytest, pytest-asyncio, Faker)

## Требования
- Python 3.11+
- PostgreSQL (pgAdmin4)
- Установленная и запущенная база данных `fastapi_db`

## Установка зависимостей

```bash
# 1. Клонировать репозиторий
git clone <https://github.com/pr1azzz/korzhov_efbo_1324_>
cd fastapi_control_work

# 2. Создать виртуальное окружение
python -m venv venv

# 3. Активировать виртуальное окружение
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Установить зависимости
pip install -r requirements.txt

# Проверка заданий осуществляется через Swagger и pytest
http://localhost:8000/docs 