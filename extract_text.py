from PIL import Image 
import pytesseract

import re
import time
import urllib
import requests

from credentials import api_key

# Main function to call
def img_text():
    
    start_time = time.time()
    print("--- %s seconds prepair---" % (time.time() - start_time))
    start_time = time.time()
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    text = pytesseract.image_to_string(Image.open("processed_file.png"))
    print("--- %s seconds read---" % (time.time() - start_time))

    URL = "https://translate.yandex.net/api/v1.5/tr/translate"
    PARAMS = {
        'key': api_key(),
        'text': text,
        'lang': "en-es"
    }
    r = requests.get(url=URL, params=PARAMS)
    data = r.text
    data = re.sub('<[^>]+>', '', data)[1:]

    print(text)
    print(data)

    return text, data
