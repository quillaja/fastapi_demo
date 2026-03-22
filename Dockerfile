FROM alpine:3.23
RUN apk add --no-cache git uv

WORKDIR /app
RUN git clone --branch v0.1.0 --depth 1 https://github.com/quillaja/fastapi_demo .

RUN uv sync --frozen --no-cache

CMD ["uv", "run", "fastapi", "run", "main.py", "--port", "8000", "--host", "0.0.0.0"]
