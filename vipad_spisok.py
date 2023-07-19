import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

time.sleep(5)

driver.get("https://suninjuly.github.io/selects1.html")

time.sleep(1)

import math


x_element = driver.find_element(By.CSS_SELECTOR, '#num1')
x = x_element.text

y_element = driver.find_element(By.CSS_SELECTOR, '#num2')
y = y_element.text

z = int(x)+int(y)

from selenium.webdriver.support.ui import Select
select = Select(driver.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(z)) # ищем элемент с текстом "Python"


final_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default")

final_button.click()

time.sleep(5)

driver.quit()