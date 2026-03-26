from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get("https://in.pinterest.com/")
driver.maximize_window()
sleep(2)

driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
sleep(5)
driver.execute_script('window.scrollTo(0,0);')
sleep(5)
driver.execute_script('window.scrollBy(0,500);') # scrolling down 500px
sleep(5)
driver.execute_script('window.scrollBy(0,-200);') # scrolling up 200px from 500px
sleep(5)
# clicking
ele = driver.find_element(By.XPATH, "(//div[@class='ADXRXN AsRsEE'])[3]/descendant::img")
driver.execute_script('arguments[0].scrollIntoView();', ele)
sleep(3)

# Clicking
click_ele = driver.find_element(By.XPATH, '(//div[text()="Join Pinterest"])[1]')
driver.execute_script('arguments[0].click();', click_ele)
sleep(3)