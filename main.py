from flask import Flask, render_template, request, redirect
import pytesseract
from PIL import Image
import os

app = Flask(__name__)

# Create an uploads directory if it doesn't exist
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    text_output = None
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            # Open the image file
            image = Image.open(filepath)
            # Use pytesseract to extract text
            text_output = pytesseract.image_to_string(image)
    return render_template('index.html', text_output=text_output)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


