# Stage 1: Builder
FROM python:3.12-slim-bookworm AS builder

# Set the working directory
WORKDIR /app

# Install build dependencies if needed (e.g., for packages with C extensions)
# RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Copy only the dependency file(s) to leverage Docker's build cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production
FROM python:3.12-slim-bookworm

# Set the working directory
WORKDIR /apps

# Copy the installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages

# Copy your application code
COPY . .

# Expose the port your application listens on (if applicable)
EXPOSE 9000

# Define the command to run your application
CMD ["python", "app.py"]
