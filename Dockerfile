# Step 1: Use an official Python runtime as a parent image
FROM python:3.12-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Set the PYTHONPATH so Python can find the app module
ENV PYTHONPATH=/app

# Step 4: Copy the requirements.txt file into the container
COPY requirements.txt /app

# Step 5: Install dependencies
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

# Step 6: Copy the rest of the application code into the container
COPY . /app/

# Step 7: Expose port 8080 for the FastAPI app
EXPOSE 8080

# Step 8: Define the command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
