import time
import os

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

time.sleep(1)

driver.get("http://suninjuly.github.io/file_input.html")


firstn = driver.find_element(By.CSS_SELECTOR, '[name="firstname"]')

firstn.send_keys("Юлия")

lastn = driver.find_element(By.CSS_SELECTOR, '[name="lastname"]')

lastn.send_keys("Иванова")


mail = driver.find_element(By.CSS_SELECTOR, '[name="email"]')

mail.send_keys("Yulia@mail.ru")

element = driver.find_element(By.CSS_SELECTOR, '[name="file"]')
current_dir = os.path.abspath(os.path.dirname(__file__))

file_path = os.path.join(current_dir, 'test.txt')

element.send_keys(file_path)



final_button = driver.find_element(By.CSS_SELECTOR, "button")

final_button.click()


time.sleep(3)

driver.quit()