FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

WORKDIR /app

COPY app/app.py ./app.py

RUN useradd --system --uid 10001 appuser

USER appuser

EXPOSE 8080

CMD ["python", "app.py"]

