from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select
import os


link = "http://suninjuly.github.io/redirect_accept.html"


try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button[type=submit]")
    button.click()
#    first_window = browser.window_handles[0]

#    confirm = browser.switch_to.alert
#    confirm.accept()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    print(y)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    time.sleep(1)

    button = browser.find_element(By.TAG_NAME, "button[type=submit]")
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
