import os
import pytesseract
from pytesseract import image_to_string
from PIL import Image
if (os.name) == "nt":
 pytesseract.pytesseract.tesseract_cmd = r''
try:
 from google.colab import files
 uploaded = files.upload()
except ModuleNotFoundError:
 print("Not using colab")

image0=Image.open('')
image0
 