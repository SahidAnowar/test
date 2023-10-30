# Use the official Python image as the base image
FROM python:3.9-slim

# Set environment variables
ENV APP_HOME /app
WORKDIR $APP_HOME

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential

# Install the 'transformers' library and other Python dependencies
RUN pip install --no-cache-dir transformers==4.13.2 fastapi uvicorn

# Copy requirements.txt and install additional Python dependencies
COPY requirements.txt $APP_HOME/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the API server code
COPY api.py $APP_HOME/

# Expose the port the app will run on
EXPOSE 8000

# Command to run the application using Uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
