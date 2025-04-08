# # Use the official Python image
# FROM python:3.9-slim

# # Set the working directory inside the container
# WORKDIR /app

# # Copy the current directory contents into the container
# COPY . /app

# # Install dependencies from requirements.txt
# RUN pip install --no-cache-dir -r app/requirements.txt

# # Expose port 5000 for the Flask app
# EXPOSE 5000

# # Command to run the Flask app
# CMD ["python", "app/app.py"]


# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port your app runs on
EXPOSE 5000

# Run the Flask app using gunicorn
CMD ["gunicorn", "app.app:app", "--bind", "0.0.0.0:5000"]
