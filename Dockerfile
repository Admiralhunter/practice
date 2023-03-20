# Use the official Python image as the base image
FROM python:3.10

# Set the working directory to /practice
WORKDIR /practice

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the default command to run the app
CMD [ "python", "practice/test.py" ]