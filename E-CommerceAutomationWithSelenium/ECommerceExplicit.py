import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise")
# time.sleep(2)
driver.implicitly_wait(2)

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)

#here we will not remove the find elements becoz empty list is also a list and it will not wait

results = driver.find_elements(By.CSS_SELECTOR,".product-action button")
count = len(results)
# print(len(results))

assert count == 3

for result in results:
    result.click()
    time.sleep(2)

# time.sleep(2)

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
# time.sleep(2)

driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
# time.sleep(2)
driver.find_element(By.CSS_SELECTOR,".promocode").send_keys("rahulshettyacademy")
# time.sleep(4)
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
# time.sleep(7)
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))

promo = driver.find_element(By.CSS_SELECTOR,".promoInfo").text

# print(promo)
assert "applied" in promo

# Sum Of the amount validation
sum1 = 0
number = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")

for no in number:
     sum1 = sum1 + int(no.text)

original = driver.find_element(By.CSS_SELECTOR,".totAmt").text
# print(sum1)
assert sum1 == int(original)
# print(__debug__)


# Assign Ques 1
discounted = driver.find_element(By.CSS_SELECTOR,".discountAmt").text
assert original >= discounted
print(__debug__)

# Assign Ques 2
list1 = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
OnscreenList = []

Onscreen = driver.find_elements(By.CSS_SELECTOR,".product-name")
for elementnumber in Onscreen:
    z = elementnumber.text
    OnscreenList.append(z)

print(OnscreenList)
# assert OnscreenList == list1
# print(__debug__)

driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
