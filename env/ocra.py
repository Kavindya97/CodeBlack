from cv2 import cv2
from PIL import Image
from pytesseract import pytesseract
from pandas import pandas
import json
path_to_tesseract= r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img_path=r"./data/img/000.jpg"

img=Image.open(img_path)
pytesseract.tesseract_cmd=path_to_tesseract
text= pytesseract.image_to_string(img)
print(text)
f= open("input.txt","w+")
f.write(text)
f.close() 

# json format
import json

def convert() :
    f = open("./img1.txt", "r")
    content = f.read()
    splitcontent = content.splitlines()

    for line in splitcontent :
        pipesplit = line.split(' | ')
        print(pipesplit)
        with open("json_log.json", 'a') as fout:
            json.dump(pipesplit, fout, indent=4)

convert()

with open("./json_log.json") as jsonFile:
    data = json.load(jsonFile)
    for x in jsonData:
        keys = x.keys()
        print(keys)
        values = x.values()
        print(values)

##This is to convert text into a jason file.

##Then we can extract the value of the key Total from the json file.
##Afterthat we can create a loop to apply this procedure to all the images (the code that can be used for looping is in the ocr.py file).
##Then we can export obtained output to a csv file. 