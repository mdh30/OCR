from process_image import process_img
from extract_text import img_text

import re
import json
import base64

from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/ocr')
def OCR():
    
    img_data = request.args.get('img')[22:]
    img_data = re.sub(' ', '+', img_data)
    img_data = bytes(img_data, 'utf=8')

    print(img_data[:100])
    
    print(type(img_data))

    with open("raw_file.png", "wb") as f:
        f.write(base64.decodebytes(img_data))

    process_img("raw_file.png", "processed_file.png")
    response = json.dumps({'ocrText': img_text()})
    return response

if __name__ == '__main__':
    app.run()