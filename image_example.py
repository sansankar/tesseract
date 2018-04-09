from PIL import Image
import pytesseract
import cv2

im = Image.open("shan.jpg")
img =cv2.imread("shan.jpg")
pytesseract.pytesseract.tesseract_cmd='C:/Program Files (x86)/Tesseract-OCR/tesseract'
text = pytesseract.image_to_string(im, lang = 'tam')


cv2.imshow("Input image",img)

print(text)
