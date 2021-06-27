from cv2 import cv2
from PIL import Image
from pytesseract import pytesseract
from pandas import pandas
#path_to_tesseract= r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#img_path=r"./data/img/000.jpg"

#img=Image.open(img_path)
#pytesseract.tesseract_cmd=path_to_tesseract
#text= pytesseract.image_to_string(img)
#print(text)
#f= open("img1.txt","w+")
#f.write(text)
#f.close() 
#c=[text]
# read image
img = cv2.imread('./data/img/003.jpg')

# configurations
config = ('-l eng --oem 1 --psm 3')

# pytessercat
pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(img, config=config)

# print text
text = text.split('\n')
#print(text)

#print(type(text))
#print(text[0])

for i in text:
    if 'Total' in i:
        print(i)

# Create a dataframe using pandas
df = pandas.DataFrame(columns=['img_num', 'Total'])

l=0
m=0
n=0
c=[]
d=[]
while n<=9:
    
    w='{}{}{}.jpg'.format(l,m,n)
    c=c.append(w)
    print(w)
    n+=1
    y = cv2.imread('./data/img/w.jpg')
# configurations
    config = ('-l eng --oem 1 --psm 3')

# pytessercat
    pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(img, config=config)

    # print text
    text = text.split('\n')
    #print(text)

    #print(type(text))
    #print(text[0])

    for i in text:
        if 'Total' in i:

            print(i)
            print(" ")

print(df)

##This is a loop which can convert image to text.