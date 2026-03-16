from selenium import webdriver
from time import sleep
drivers = [webdriver.Chrome(), webdriver.Firefox(), webdriver.Edge()]
for d in drivers:
    driver = d()
    driver.get("https://google.com")
    sleep(2)
    driver.quit()
