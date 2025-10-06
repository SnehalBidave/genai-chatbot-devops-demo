# Use a lightweight Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy only the dependency file first (for caching)
COPY requirements.txt .

# Install dependencies without cache to keep image small
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose Flask port
EXPOSE 5000

# Use Gunicorn for production (more stable than Flask dev server)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
