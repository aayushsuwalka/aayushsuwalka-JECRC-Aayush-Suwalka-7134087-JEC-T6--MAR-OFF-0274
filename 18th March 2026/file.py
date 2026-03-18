from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(2)

male=driver.find_element(By.ID, 'male')
male.click()
print(male.is_displayed())
print(male.is_enabled())

check = driver.find_element(By.XPATH, '//label[text()="Monday"]/preceding-sibling::input')
check.click()
print(check.is_selected())
mon_check = driver.find_element(By.XPATH, "//input[@id='monday']/following-sibling::label")
print(mon_check.text)
sleep(3)
driver.quit()