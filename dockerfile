# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install uv 
RUN pip install uv

# Copy the dependency files
COPY pyproject.toml uv.lock ./

# Synchronize dependencies using uv
RUN uv sync 

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]