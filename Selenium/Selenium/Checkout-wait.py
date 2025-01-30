import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@class='search-keyword']").send_keys("ber")
time.sleep(2)
products=driver.find_elements(By.XPATH,"//div[@class='product']")
for product in products:
    product.find_element(By.XPATH,"div/button").click()  #why div/button?because we user product instead of driver and we are looping inside a blocl

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()

driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[text()='Apply']").click()

x=driver.find_element(By.CSS_SELECTOR,".promoInfo").text
assert x=="Code applied ..!"

#git branch save
