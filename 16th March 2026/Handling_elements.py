from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# driver.maximize_window()
#
# name = driver.find_element(By.ID, 'name')
# name.clear()
# name.send_keys('Aayush')
# sleep(1)
# email = driver.find_element(By.XPATH, '//input[@placeholder="Enter EMail"]')
# email.clear()
# email.send_keys('aayushsuwalka@gmail.com')
# sleep(5)
# print(name.get_attribute('placeholder'))
# print(name.get_attribute('value'))
#
# driver.quit()

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
driver.find_element(By.ID, 'male').click()
driver.find_element(By.XPATH, '//label[text()="Monday"]/preceding-sibling::input').click()
monday_checkbox = driver.find_element(By.XPATH, '//input[@id="monday"]/following-sibling::label')
print(monday_checkbox.text)

sleep(5)
# driver.get("https://www.amazon.com/")
# driver.maximize_window()
# sleep(5)

# search = driver.find_element(By.ID, "twotabsearchtextbox")
# search.clear()
# search.send_keys("watches for men", Keys.ENTER)
# sleep(2)

driver.quit()