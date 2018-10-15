# Optical Character Recognition
Project on Multilingual Optical Character Recognition

#### Tasks
 - [X] Process image - Focus on the text area, removing all corners and extra features
 - [x] Extract text - Using tesseract, extract text from the image
 - [x] Translate - Translate English text to Spanish
 - [x] Server - Flask server to integrate Python modules with the frontend
 - [x] Website - Basic website to upload image and display OCR text and translated text
 - [ ] Document server code

#### APIs
 - [Yandex API](https://tech.yandex.com/translate/)
 ```python
    # Url
    URL = "https://translate.yandex.net/api/v1.5/tr/translate"
    
    # Parameters
    # key: API KEY
    # text: Text to translate
    # land: from - to language
    PARAMS = {
        'key': api_key,
        'text': text,
        'lang': "en-es"
    }
    
    # Request
    r = requests.get(url=URL, params=PARAMS)
    
    # Parse response
    data = r.text
    data = re.sub('<[^>]+>', '', data)[1:]
 ```

#### Run

 - Install requirements
```
pip install -r requirements.txt
```
 - Start the server
```
python server.py
```
 - Run the website
 - Upload image

 #### Contributors

:heart_eyes: [Nishant Rodrigues ](https://github.com/nishnash54)