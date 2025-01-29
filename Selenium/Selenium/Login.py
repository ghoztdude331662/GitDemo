import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")

driver.find_element(By.LINK_TEXT,"Forgot password?").click()

driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Hello@123")
driver.find_element(By.ID,"confirmPassword").send_keys("Hello@123")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(4) button").click()

time.sleep(2)