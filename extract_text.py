from PIL import Image 
import pytesseract
import time
import urllib
start_time = time.time()
start_time2 = time.time()
print("serial execution")
print("--- %s seconds prepair---" % (time.time() - start_time))
start_time = time.time()
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
a = pytesseract.image_to_string(Image.open('text.jpg'))
print(a)
print("--- %s seconds read---" % (time.time() - start_time))
#print("--- %s seconds read---" % (time.time() - start_time2))
