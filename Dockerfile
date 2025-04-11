FROM python:3.9-slim

# Update package lists and install Tesseract OCR and its development libraries.
RUN apt-get update && apt-get install -y tesseract-ocr libtesseract-dev

# Set the working directory.
WORKDIR /app

# Copy requirements and install Python dependencies.
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application.
COPY . .

# Expose port 5000.
EXPOSE 5000

# Run the Flask app.
CMD ["python", "main.py"]
