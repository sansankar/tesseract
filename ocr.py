import pytesseract
from PIL import Image

img = Image.open('sa.png')
pytesseract.pytesseract.tesseract_cmd='C:/Program Files (x86)/Tesseract-OCR/tesseract'
result = pytesseract.image_to_string(img)

with open('output.txt', mode='w')as file:
    file.write(result)
    print('san check output file')
