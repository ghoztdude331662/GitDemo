import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("Ind")
time.sleep(2)

countries=driver.find_elements(By.CLASS_NAME,"ui-menu-item")
for country in countries:
    if country.text=="India":
        country.click()
        break
cname=driver.find_element(By.ID,"autosuggest").get_attribute("value")

assert cname=="India"
