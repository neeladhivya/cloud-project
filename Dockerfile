# 1. Start with an official Python base image
FROM python:3.9-slim

# 2. Set the "working directory" inside the container
WORKDIR /app

# 3. Copy the requirements file in first
COPY requirements.txt .

# 4. Install the Python libraries
RUN pip install -r requirements.txt

# 5. Copy the rest of your project files (just app.py)
COPY . .

# 6. Tell Docker what port your app runs on
EXPOSE 5000

# 7. The command to run your app when the container starts
CMD ["python", "app.py"]