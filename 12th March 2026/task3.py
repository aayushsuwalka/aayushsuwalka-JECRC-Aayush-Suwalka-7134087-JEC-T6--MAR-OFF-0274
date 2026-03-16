from selenium import webdriver
from time import sleep
drivers = [webdriver.Chrome, webdriver.Firefox, webdriver.Edge]
for d in drivers:
    driver = d()
    driver.get("https://www.google.com/")
    sleep(5)

    print(f'Current URL is: {driver.current_url}')
    print(f'Driver name: {driver.name}')
    print(f'Driver title: {driver.title}')
    print('--------------------------------')
    driver.quit()
