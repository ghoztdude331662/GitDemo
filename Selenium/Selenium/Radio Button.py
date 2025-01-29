from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice")

radiobuttons=driver.find_elements(By.NAME,"radioButton")
for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value")=="radio2":
        radiobutton.click()
        assert radiobutton.is_selected()
        break


driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_selected()



