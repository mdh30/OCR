from process_image import process_img
from extract_text import img_text

import re
import json
import base64

# import flask modules
# Request - gets details for the request
# Flask - creates the flask app
from flask import Flask, request

# import flask_cors modules
# CORS - enable Cross Origin Resource Sharing
from flask_cors import CORS

# Create the app and enable CORS
app = Flask(__name__)
CORS(app)

# Route at which the request is processed
# http://localhost:5000/ocr
@app.route('/ocr')
def OCR():

    # Get data from the request
    # Convert base64 encoded to png    
    img_data = request.args.get('img')[22:]
    img_data = re.sub(' ', '+', img_data)
    img_data = bytes(img_data, 'utf=8')

    # Save image as raw_file.png
    with open("raw_file.png", "wb") as f:
        f.write(base64.decodebytes(img_data))

    # Process image file
    process_img("raw_file.png", "processed_file.png")

    # Extract text and translate
    # text - extracted text
    # data - translated text
    text, data = img_text()

    # Convert data to a json response
    response = json.dumps({'ocrText': text, 'trans': data})

    # Return json response
    return response

if __name__ == '__main__':
    app.run()