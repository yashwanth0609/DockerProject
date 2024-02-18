# Use the official Python image from Docker Hub
FROM python:3.8-alpine

# Set the working directory inside the container
WORKDIR /home

# Create the /home/data directory inside the container
RUN mkdir -p data

RUN mkdir -p output

# Set the working directory to /home/data
WORKDIR /home/data

# Copy the contents of the host's /home/data directory into the container
COPY . /home/data

# Run the command when the container starts
CMD ["python", "project3.py"]
