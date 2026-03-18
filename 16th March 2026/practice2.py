from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get('https://www.flipkart.com/')
sleep(2)
search = driver.find_element(By.NAME, "q")
search.send_keys('mobiles')
search.send_keys(Keys.RETURN)
sleep(2)

checkboxes = driver.find_element(By.XPATH, '(//div[@class="buvtMR"]/preceding-sibling::div[@class="ybaCDx"])[1]')
checkboxes.click()
sleep(2)
driver.quit()
