from PIL import Image 
import pytesseract
import time
import urllib

# Main function to call
def img_text():
    
    start_time = time.time()
    print("--- %s seconds prepair---" % (time.time() - start_time))
    start_time = time.time()
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    text = pytesseract.image_to_string(Image.open("processed_file.png"))
    print(text)
    print("--- %s seconds read---" % (time.time() - start_time))
    
    return text
