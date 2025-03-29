# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Create and activate a virtual environment
RUN python -m venv /opt/venv

# Set the environment variable to use the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Install the dependencies in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port 8080 for the FastAPI app
EXPOSE 8080

# Command to run the app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

# Expose the port that your app will run on
EXPOSE 8000

# Define the command to run your app (this should match how your app is run)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
