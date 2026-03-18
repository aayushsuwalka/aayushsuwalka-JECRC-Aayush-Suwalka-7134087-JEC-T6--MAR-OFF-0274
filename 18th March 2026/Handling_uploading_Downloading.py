from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(5)
choose_file = driver.find_element(By.ID, 'file-uplaod')
choose_file.send_keys('"C:\Users\aayus_ucf5jw3\OneDrive\Pictures\Screenshots 1\Screenshot 2026-01-29 120949.png"')
