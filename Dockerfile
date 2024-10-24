FROM python:3.9-slim
WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
