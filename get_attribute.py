import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

time.sleep(5)

driver.get("http://suninjuly.github.io/get_attribute.html")

time.sleep(1)

#считаем уравнение

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

img = driver.find_element(By.CSS_SELECTOR, "#treasure")
number = img.get_attribute("valuex")
x = number
y = calc(x)

textarea = driver.find_element(By.CSS_SELECTOR, '#answer')

textarea.send_keys(y)

time.sleep(2)


submit_button1 = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")

submit_button1.click()


submit_button2 = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
submit_button2.click()

final_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default")

final_button.click()


time.sleep(15)

driver.quit()