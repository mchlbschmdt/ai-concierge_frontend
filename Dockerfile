# Step 1: Use an official Python runtime as a parent image
FROM python:3.12-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Step 4: Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Step 5: Copy the rest of the application code into the container at /app
COPY . /app/

# Step 6: Expose port 8080 for the FastAPI app
EXPOSE 8080

# Step 7: Define the command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

