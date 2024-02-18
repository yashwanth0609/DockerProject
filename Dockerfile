# Use the official Python image from Docker Hub
FROM python:3.8-alpine

WORKDIR /home/

COPY . .

WORKDIR /home/data

COPY . .

# Create the /home/output directory inside the container
RUN mkdir -p /home/output

# Run the command when the container starts
CMD ["python", "/home/project3.py"]
