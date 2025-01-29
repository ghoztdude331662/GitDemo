from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.dom import get_attributes

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice")

#driver.find_element(By.ID,"checkBoxOption1").click()
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value")=="option1":
        checkbox.click()
        assert checkbox.is_selected()
        break


