FROM python:3.11-slim as builder
WORKDIR /backend
RUN pip install --no-cache-dir --upgrade poetry
COPY poetry.lock pyproject.toml ./
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --without dev

FROM python:3.11-slim
WORKDIR /backend
COPY --from=builder /backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
COPY . .

EXPOSE 80

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]