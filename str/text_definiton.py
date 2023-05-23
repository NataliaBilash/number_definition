import pytesseract
from PIL import Image

#распознование языка и запись его ниже

#custom_oem_psm_config = r'--oem 3 --psm 6' #улучшение точности config=custom_oem_psm_config config='--psm 6 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def text_definition(image):
    text = pytesseract.image_to_string(image) 
    print(text)




