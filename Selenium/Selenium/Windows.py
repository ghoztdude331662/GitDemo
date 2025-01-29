from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.XPATH,"//div[@class='example']/a").click()

#New Window Switching

windowOpen=driver.window_handles
driver.switch_to.window(windowOpen[1])
text=driver.find_element(By.CSS_SELECTOR, "div[class='example'] h3").text
print(text)
driver.close()
driver.switch_to.window(windowOpen[0])
oldwin=driver.find_element(By.XPATH,"//div[@class='example']/h3").text
print(oldwin)

