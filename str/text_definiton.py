import pytesseract
from PIL import Image
import re

#Данный модуль предназначен для распознавания текста с уже подготовленной области, картинки, которая вырезается в основном модуле number_definition.py
#This module recognizes the test from the picture received in the main module number_definition.py

#улучшение точности custom_oem_psm_config = r'--oem 3 --psm 13 -c tessedit_char_whitelist=АВЕКМНОРСТУХ0123456789' буквы только те, которые встречаются в автомобильных номерах

def text_definition(image):
    custom_oem_psm_config = r'--oem 3 --psm 13 -c tessedit_char_whitelist=АВЕКМНОРСТУХ0123456789'
    text = pytesseract.image_to_string(image, config=custom_oem_psm_config, lang='rus')
    # предназначено для уборки шума из английского текста
    # text_filter = re.compile('[^a-zA-Z0-9 ]')
    # text_filter = text_filter.sub('', text)
    # text_filter = text_filter.replace(' ', '')
    print("Recognized license plate: ")
    print(text)
    
    return text
    
#запись номеров в текстовый файл
def write_file(definition_carplate):
    output_file = open("outputs/output.txt", "a")
    output_file.write(definition_carplate+'\n')
    output_file.close()

    return print("Carplate written in file.")