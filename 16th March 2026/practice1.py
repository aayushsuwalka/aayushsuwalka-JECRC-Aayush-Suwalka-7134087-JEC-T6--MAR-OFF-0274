from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
days = driver.find_elements(By.XPATH, '//div[@class="form-check form-check-inline"]/input[@type="checkbox"]')
print(type(days))
for day in days:
    day.click()
    sleep(2)
sleep(3)
for day in days[::-1]:
    day.click()
    sleep(2)
driver.quit()