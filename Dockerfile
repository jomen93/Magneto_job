# Use a python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy the neccesary files
COPY . .

# Dependencies instalation
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port to FastAPI
EXPOSE 8000

# Run!
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
