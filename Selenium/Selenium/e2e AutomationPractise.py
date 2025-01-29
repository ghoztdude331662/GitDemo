import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)

#Radio Button
radios=driver.find_elements(By.NAME,"radioButton")
for radio in radios:
    if radio.get_attribute("value")=="radio2":
        radio.click()
        assert radio.is_selected()
        break
#Suggestion class example
driver.find_element(By.ID,"autocomplete").send_keys("ind")

suggestionitems=driver.find_elements(By.CSS_SELECTOR,".ui-menu-item")
for suggestion in suggestionitems:
    if suggestion.text=="India":
        suggestion.click()

#dropdown

dropdown=driver.find_element(By.ID,"dropdown-class-example")
select=Select(dropdown)
select.select_by_visible_text("Option2")

#checkbox

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value")=="option3":
        checkbox.click()


#switch window example

driver.find_element(By.ID,"openwindow").click()
time.sleep(5)
windowopen=driver.window_handles
print(windowopen)
driver.switch_to.window(windowopen[1])
textw=driver.find_element(By.XPATH,"//div[@class='button float-left']//a[@class='main-btn']").text
print(textw)









