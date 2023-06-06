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

option = Options()
option.add_argument("--disable-infobars") 
driver = webdriver.Chrome(ChromeDriverManager().install())
# https://avtocod.ru/
driver.get('https://avtocod.ru/')

elem  =  driver.find_element(By.CLASS_NAME,  'search-block__field' )
elem.send_keys('А222АА78' + Keys.RETURN)

share =  driver.find_element(By.CLASS_NAME,  'search-block__btn' )
share.click()

time.sleep(4)