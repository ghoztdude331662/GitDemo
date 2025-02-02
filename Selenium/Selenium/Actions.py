from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#Mouse Hover Action
action= ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Reload")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click()


#First git
#Second Guy Git