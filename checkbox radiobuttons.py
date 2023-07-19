import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

time.sleep(5)

driver.get("https://suninjuly.github.io/math.html")

time.sleep(1)


import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = driver.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap')
x = x_element.text
y = calc(x)


textarea = driver.find_element(By.CSS_SELECTOR, '.form-control')

textarea.send_keys(y)


submit_button1 = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")

submit_button1.click()


submit_button2 = driver.find_element(By.CSS_SELECTOR, "#robotsRule")

submit_button2.click()


final_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default")

final_button.click()

time.sleep(5)

driver.quit()