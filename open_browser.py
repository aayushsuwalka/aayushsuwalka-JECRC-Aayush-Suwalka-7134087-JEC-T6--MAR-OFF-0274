from selenium import webdriver
from time import sleep
# driver = webdriver.Chrome()
# sleep(5)
# driver = webdriver.Edge()
# sleep(5)
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# driver = webdriver.Firefox()
sleep(5)
driver.get('https://supertails.com/')
sleep(5)
driver.maximize_window()
sleep(2)
# driver.minimize_window()
# sleep(2)


driver.back()
sleep(2)
driver.forward()
sleep(2)
print(driver.current_url)
print(driver.title)
print(driver.name)
# driver = webdriver.Firefox()
driver.quit()
