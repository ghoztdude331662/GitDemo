import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise")
driver.implicitly_wait(5)

#Clicking banner
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()

#new window
windowL=driver.window_handles
driver.switch_to.window(windowL[1])

#Grab Text
email=driver.find_element(By.XPATH,"//div[@class='col-md-8']/p[2]").text
parseEmail = email.split(" at ")[1].split(" ")[0]

print(email)
print(parseEmail)

driver.close()
#switch back to previous window
driver.switch_to.window(windowL[0])

#passing values
driver.find_element(By.ID,"username").send_keys(parseEmail)
driver.find_element(By.ID,"password").send_keys("Password")

#driver.find_element(By.XPATH,"//input[@value='user']").click()




driver.find_element(By.ID,"terms").click()
driver.find_element(By.ID,"signInBtn").click()


wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
print(driver.find_element(By.XPATH,"//div[@class='alert alert-danger col-md-12']").text)







