FROM python:3

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/src

# Make port 8088 available to the world outside this container
EXPOSE 8088

# Run main.py when the container launches
CMD ["python", "main.py"]