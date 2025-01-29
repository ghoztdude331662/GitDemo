import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.ID,"tinymce")))
driver.find_element(By.CLASS_NAME,"tox tox-silver-sink tox-tinymce-aux tox-platform-touch")

