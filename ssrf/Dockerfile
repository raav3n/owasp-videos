# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the files to the container
ADD . /app

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the Flask application runs
EXPOSE 5000

# Set the environment variables
ENV FLASK_APP=ssrf-owasp.py

# Run the Flask application when the container launches
CMD ["python","ssrf-owasp.py"]