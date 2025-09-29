# Use a lightweight Python image
FROM python:3.11-slim

# set working directory
WORKDIR /app

# Install any OS-level dependencies (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Download NLTK data (punkt, stopwords) into a known location
RUN python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

# Expose port (Flask / gunicorn default)
EXPOSE 5000

# Set environment variables
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Use gunicorn as the entrypoint (adjust the app import path as needed)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app3:app"]
