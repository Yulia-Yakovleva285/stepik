import time

import math

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait (driver, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), '$100'))

button = driver.find_element(By.CSS_SELECTOR, "#book").click()


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = driver.find_element(By.CSS_SELECTOR, 'span#input_value.nowrap')
x = x_element.text
y = calc(x)

textarea = driver.find_element(By.CSS_SELECTOR, '.form-control')

textarea.send_keys(y)

final_button = driver.find_element(By.CSS_SELECTOR, "#solve")

final_button.click()

time.sleep(15)

driver.quit()