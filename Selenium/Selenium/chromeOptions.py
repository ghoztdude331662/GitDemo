

from selenium import webdriver

chromeoptions=webdriver.ChromeOptions()
chromeoptions.add_argument("--start-maximized")
chromeoptions.add_argument("headless")
chromeoptions.add_argument("--ignore-certificate-errors")
driver=webdriver.Chrome(options=chromeoptions)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)