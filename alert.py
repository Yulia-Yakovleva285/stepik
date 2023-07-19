import time

import math

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

time.sleep(1)

driver.get("http://suninjuly.github.io/alert_accept.html")


button = driver.find_element(By.CSS_SELECTOR, 'button')
button.click()

time.sleep(1)

confirm = driver.switch_to.alert
confirm.accept()



def answer(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = driver.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap')
x = x_element.text
y = answer(x)

textarea = driver.find_element(By.CSS_SELECTOR, '.form-control')

textarea.send_keys(y)

final_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")

final_button.click()

time.sleep(15)

driver.quit()