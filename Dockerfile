# Use the Python 3.8 base image
FROM python:3.8

# Create and set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . .

# Set any environment variables here (if needed)
ENV FILEPATH=mockupinterviewdata.csv


# Run the application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "interview.wsgi:application"]

# Expose the port that the application listens on
EXPOSE 8000
