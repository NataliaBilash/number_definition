from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

#сохранение страницы сайта, чтобы он не включил защиту от роботов


def parsing(carplate):
    option = Options()
    option.add_argument("--disable-infobars") 
    # https://avtocod.ru/
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://avtocod.ru/')
    #заполнение поля и нажание на кнопку
    find_text_field  =  driver.find_element(By.CLASS_NAME,  'search-block__field' )
    find_text_field.send_keys(carplate + Keys.RETURN)

    find_button =  driver.find_element(By.CLASS_NAME,  'search-block__btn' )
    find_button.click()

    time.sleep(60)
    url = driver.current_url
    return url
    