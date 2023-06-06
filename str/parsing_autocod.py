import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


# код заоса станицы 
# url = "https://avtocod.ru/"

# headers = {
#     "accept": "*/*",
#     "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
# }

# #получение кода страницы
# req = requests.get(url, headers=headers)
# src = req.text
# #print(src)



carplate = "A222AA75"
driver = webdriver.Chrome("chromedriver")
driver.get("https://avtocod.ru/")
driver.find_element(By.CLASS_NAME,"search-block__field js-gos js-input").send_keys(carplate)
driver.find_element("link_text","Проверить авто").click()
# ждем завершения состояния готовности

#сохранение сайта
# with open("sites_files/index.html", "w") as file:
#     file.write(src)

# with open("sites_files/index.html") as file:
#     src = file.read()

# soup = BeautifulSoup(src, "lxml")