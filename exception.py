import time

import math

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

time.sleep(1)

driver.get("http://suninjuly.github.io/cats.html")

time.sleep(5)

driver.quit()