# Use slim Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app and templates
COPY . .

# Expose port
EXPOSE 5000

# Start app
CMD ["python", "app.py"]
