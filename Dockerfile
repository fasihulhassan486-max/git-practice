# Step 1: Use an official Python image
FROM python:3.10-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Copy project files
COPY . .

# Step 4: Run your script
CMD ["python", "hello.py"]
