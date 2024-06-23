FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy

COPY . /app
WORKDIR /app
RUN pip install .
RUN playwright install chromium