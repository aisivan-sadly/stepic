from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    def calc(x):
        return str()

    browser = webdriver.Chrome()
    browser.get(link)
    print("Hi")

    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    x1_element = browser.find_element(By.ID, "num2")
    x1 = x1_element.text
    y = str(int(x1)+int(x))

    print(y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(y)

    time.sleep(1)

    button = browser.find_element(By.TAG_NAME, "button[type=submit]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
