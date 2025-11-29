# Use an official Python image as the base
FROM python:3.12

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the working directory
COPY . .

# Ensure templates and static are being copied
COPY app/templates /app/templates
COPY app/static /app/static

ENV FLASK_APP=app

EXPOSE 5000

CMD ["/bin/sh", "-c", "flask run --host=0.0.0.0 --port=5000"]