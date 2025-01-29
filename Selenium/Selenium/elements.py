import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Rahul")#css selector
driver.find_element(By.NAME,"email").send_keys("rahul@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Rahul1")
driver.find_element(By.ID,"exampleCheck1").click()
#driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']/option[text()='Male']").click()
#driver.find_element(By.XPATH,"//select[@id='exampleFormControlSelect1']/option[1]").click()
#Select
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_index(0)
driver.find_element(By.XPATH,"//input[@value='option1']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()#xpath
msg=driver.find_element(By.CLASS_NAME,"alert").text
print(msg)
assert "The Form" in msg


time.sleep(2)