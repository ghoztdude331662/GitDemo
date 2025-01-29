import time
from wsgiref.validate import assert_

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.find_element(By.XPATH,"//span[@class='sort-icon sort-descending']").click()

veggienames=driver.find_elements(By.CSS_SELECTOR,"tbody tr td:nth-child(1)")
browsersortedveggi=[]
for veggi in veggienames:
    browsersortedveggi.append(veggi.text)

print(browsersortedveggi)

listsorted=browsersortedveggi.copy()  #For copying

browsersortedveggi.sort()
assert listsorted==browsersortedveggi