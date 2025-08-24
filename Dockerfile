# Professional Dockerfile for CookieSpy (CLI & Flask Webapp)
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip \
    && pip install -e . \
    && pip install flask

# Expose Flask default port
EXPOSE 5000

# Entrypoint script (choose CLI or webapp)
# Default: run Flask webapp
CMD ["python", "src/cookiespy/webapp.py"]

# To run CLI, override CMD in docker run:
# docker run --rm cookiespy python -m cookiespy.cli --help
