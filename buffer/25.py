from selenium import webdriver
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "http://suninjuly.github.io/explicit_wait2.html"

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    def mm():
        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        y = calc(x)
        print(y)
        input1 = browser.find_element(By.ID, "answer")
        input1.send_keys(y)


    browser: WebDriver = webdriver.Chrome()
    browser.implicitly_wait(12)
    browser.get(link)

    accept1 = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    print(accept1)
    if accept1:
        print(1)

    button1 = browser.find_element(By.ID, "book")
    button1.click()

    mm()

    time.sleep(1)

    button = browser.find_element(By.TAG_NAME, "button[type=submit]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
