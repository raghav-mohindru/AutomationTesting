import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID,"name").send_keys("Raghav")
time.sleep(3)

driver.find_element(By.ID,"alertbtn").click()
time.sleep(3)

alert = driver.switch_to.alert
alertText = alert.text

assert "Raghav" in alertText

print(alertText)
alert.accept()
