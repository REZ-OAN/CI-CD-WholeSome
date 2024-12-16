FROM python:3.9-slim

WORKDIR /app

# Install netcat and any other dependencies
RUN apt-get update && \
    apt-get install -y \
    netcat-openbsd \
    iputils-ping && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Ensure wait-for-it.sh is executable
RUN chmod +x wait-for-it.sh
RUN chmod +X start.sh

