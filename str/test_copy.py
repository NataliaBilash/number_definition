import pytesseract
from PIL import Image
import re

#распознование языка и запись его ниже

#улучшение точности config=custom_oem_psm_config config='--psm 6 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def test(image):
    text = pytesseract.image_to_string(image, lang='rus')
    print(text)
    return text
