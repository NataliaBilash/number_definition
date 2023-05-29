import pytesseract
from PIL import Image
import re

#распознование языка и запись его ниже

#улучшение точности config=custom_oem_psm_config config='--psm 6 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def text_definition(image):
    #custom_oem_psm_config = r'--psm 6 --oem 13'
    text = pytesseract.image_to_string(image)
    text_filter = re.compile('[^a-zA-Z0-9 ]')
    text_filter = text_filter.sub('', text)
    text_filter = text_filter.replace(' ', '')
    print("Recognized license plate: ")
    print(text_filter)
    
    return text_filter
    

def write_file(definition_carplate):
    output_file = open("output.txt", "a")
    output_file.write(definition_carplate+'\n')
    output_file.close()

    return print("Carplate written in file.")



