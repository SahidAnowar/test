FROM python:3.9-slim

# Set environment variables
ENV APP_HOME /app
WORKDIR $APP_HOME

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential

# Copy requirements.txt and install the dependencies
COPY requirements.txt $APP_HOME/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the API server code
COPY api.py $APP_HOME/

# Expose the port the app will run on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
