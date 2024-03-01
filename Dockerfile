FROM python:3.10.8-slim-bullseye as build-python

RUN apt-get update && \
    apt-get install -y \
    libpq-dev \
    python3-dev \
    gcc \
    # Cleanup apt cache
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
WORKDIR /app/
RUN pip install -r requirements.txt

FROM python:3.10.8-slim-bullseye

RUN apt-get update && \
    apt-get install -y \
    libpq-dev \
    # Cleanup apt cache
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/app

COPY --from=build-python /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=build-python /usr/local/bin/ /usr/local/bin/

COPY . .

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "core.asgi:application" ,"-k","uvicorn.workers.UvicornWorker", "--log-level=debug"]

