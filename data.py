import argparse
import io
import os
import re
from google.cloud.vision import types
import pandas as pd
from google.cloud import vision
from google.cloud.vision import ImageAnnotatorClient

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'atomic-key-273611-8a5180854a67.json'
client = ImageAnnotatorClient()

FOLDER_PATH = r'C:\Users\Pushpraj\Desktop\Finish'
IMAGE_FILE = 'pic.jpg'
FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

with io.open(FILE_PATH, 'rb') as image_file:
    content = image_file.read()
    
image = vision.types.Image(content=content)
response = client.document_text_detection(image=image)


docText = response.full_text_annotation.text


with open('textfile.txt',mode='w') as file:
   file.write(docText)

print("see the text file")
