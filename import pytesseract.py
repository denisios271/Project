import pytesseract
import cv2
from PIL import Image


image = cv2.imread("sample1.jpg")

string = pytesseract.image_to_string(image)

print(string)
