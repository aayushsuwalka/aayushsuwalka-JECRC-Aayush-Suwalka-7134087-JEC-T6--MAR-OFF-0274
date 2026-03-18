from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(5)
country_dropdown = driver.find_element(By.ID, 'country')
dropdown = Select(country_dropdown)
dropdown.select_by_value('india')
sleep(2)

