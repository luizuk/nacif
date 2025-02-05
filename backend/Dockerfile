# Use official Python image from DockerHub
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY ../requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the backend folder to the working directory
COPY . /app/backend

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
