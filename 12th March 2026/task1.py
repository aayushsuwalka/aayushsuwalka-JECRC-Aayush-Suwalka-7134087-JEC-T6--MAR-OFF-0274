from selenium import webdriver
from time import sleep

opts= webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get("https://supertails.com/")
driver.maximize_window()
sleep(2)
# driver.minimize_window()
# sleep(2)
# driver.back()
# sleep(2)
# driver.forward()
# sleep(2)
#
# driver.refresh()
# sleep(2)
print(f'Driver Tittle : {driver.title}')
print(f'Driver Url : {driver.current_url}')
print(f'Driver Name : {driver.name}')



driver.quit()