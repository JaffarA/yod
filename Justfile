format:
    poetry run black .
    poetry run isort .

lint:
    poetry run ruff check .
    poetry run mypy .

run:
    poetry run uvicorn main:app --reload

test:
    poetry run pytest .
