import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@class='search-keyword']").send_keys("ber")
time.sleep(2)
#list verification

expectList=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
productPage=driver.find_elements(By.XPATH,"//div[@class='product']")
actualList=[]
for productL in productPage:
    actualList.append(productL.find_element(By.XPATH, "h4").text)
print(actualList)
print(expectList)

assert actualList == expectList



time.sleep(2)
products=driver.find_elements(By.XPATH,"//div[@class='product']")
for product in products:
    product.find_element(By.XPATH,"div/button").click()  #why div/button?because we user product instead of driver and we are looping inside a blocl

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()

driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#Summation
sumT=driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
tot=0
for su in sumT:
    tot=tot+int(su.text)
total=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert tot==total




driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[text()='Apply']").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))  # Correct


x=driver.find_element(By.CSS_SELECTOR,".promoInfo").text
assert x=="Code applied ..!"

totalamount= driver.find_element(By.XPATH, "//span[@class='totAmt']").text
afterdiscount=driver.find_element(By.XPATH,"//span[@class='discountAmt']").text
assert afterdiscount<totalamount


