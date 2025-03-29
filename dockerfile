# Use an official Python runtime as the base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies for building the environment (optional, based on needs)
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install pip, virtualenv, and dependencies
RUN pip install --upgrade pip \
    && pip install virtualenv \
    && virtualenv /opt/venv \
    && /opt/venv/bin/pip install -r requirements.txt

# Copy the rest of the application files
COPY . /app/

# Ensure the virtual environment is activated by default
ENV PATH="/opt/venv/bin:$PATH"

# Expose the port that your app will run on
EXPOSE 8000

# Define the command to run your app (this should match how your app is run)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
