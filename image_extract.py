import os
from pytesseract import pytesseract

tesseract_path = "/usr/bin/tesseract"

pytesseract.tesseract_cmd = tesseract_path

text = pytesseract.image_to_string("purchase_order.png")

print(text)
