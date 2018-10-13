# from process_image import process_img
from extract_text import img_text

import json

from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/ocr')
def OCR():
    # process_img()
    a = img_text()
    a = json.dumps({'movie': a})
    return a

if __name__ == '__main__':
    app.run()