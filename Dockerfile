FROM python:3.12-slim

# Create app directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the port FastAPI runs on
EXPOSE 8000

# Run the API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
