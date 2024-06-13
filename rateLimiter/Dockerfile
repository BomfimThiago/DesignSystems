
FROM python:3.10-slim


RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*


RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python -


ENV PATH="/opt/poetry/bin:$PATH"

WORKDIR /app


COPY poetry.lock pyproject.toml /app/

RUN poetry install


COPY . .

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
