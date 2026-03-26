import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

folder = os.path.join(os.getcwd(), 'screenshots')
os.makedirs(folder, exist_ok=True)
driver = webdriver.Chrome()
driver.get("https://in.pinterest.com/")
action = ActionChains(driver)
driver.maximize_window()
sleep(2)
# C:\Users\aayus_ucf5jw3\OneDrive\Desktop\Project_Selenium\
driver.save_screenshot(f'{folder}/full_page.png')
sleep(2)
ele = driver.find_element(By.XPATH, "(//div[@class='ADXRXN AsRsEE'])[3]/descendant::img")
action.scroll_to_element(ele).perform()
ele.screenshot(f'{folder}/cheery_red.png')
sleep(1)
