import pytesseract
from PIL import Image

textData = ""

for i in range(1,174):

    a = "D:\\tasrif\\T (" + str(i) + ").jpg"
    img = Image.open(a)
    pytesseract.pytesseract.tesseract_cmd="D:\\ocr\\tesseract.exe"
    result = pytesseract.image_to_string(img,lang="ara")
    with open('converted image.txt' , mode='w',encoding='utf-8') as textFile:
        textFile.write(result)
        #print(result)
        textData = textData + result 


print(textData)
