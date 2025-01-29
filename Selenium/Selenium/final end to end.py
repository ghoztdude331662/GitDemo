import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
chromeoptions=webdriver.ChromeOptions()
chromeoptions.add_argument("--start-maximized")
driver=webdriver.Chrome(options=chromeoptions)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)

driver.find_element(By.LINK_TEXT,"Shop").click()


#cardTitle=driver.find_elements(By.CSS_SELECTOR,".card-title")
#for card in cardTitle:
#    if card.text=="Blackberry":
 #       card.click()

cardTitle=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for card in cardTitle:
    prodname=card.find_element(By.CSS_SELECTOR,".card-title").text
    if prodname=="Blackberry":
        card.find_element(By.XPATH, "//button[text()='Add ']").click()

checkout=driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").text

assert "1" in checkout

driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

driver.find_element(By.ID,"country").send_keys("in")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='suggestions']/ul")))
#wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))

countries=driver.find_elements(By.XPATH,"//div[@class='suggestions']/ul/li/a")


for c in countries:
    if c.text=="India":
        c.click()
        break

#driver.find_element(By.LINK_TEXT,"India").click()

driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
driver.find_element(By.XPATH,"//input[@value='Purchase']").click()

msg=driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
print(msg)

assert "Success! Thank you!" in msg













