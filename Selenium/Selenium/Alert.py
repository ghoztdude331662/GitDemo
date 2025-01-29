import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice")
driver.find_element(By.CSS_SELECTOR,"input[name='enter-name']").send_keys("Rahul")
driver.find_element(By.ID,"alertbtn").click()
alert=driver.switch_to.alert
name=alert.text
assert "Rahul" in name
alert.accept()


time.sleep(2)
