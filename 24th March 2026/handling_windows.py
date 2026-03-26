from pydoc import parentname

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
sleep(5)
parent_window = driver.current_window_handle
driver.find_element(By.XPATH, '//a[text()="Click Here"]').click()
sleep(5)
all_windows = driver.window_handles
print(len(all_windows))
driver.switch_to.window(all_windows[-1])
assert 'New' in driver.find_element(By.CLASS_NAME, 'example').text
print('done')
driver.switch_to.window(parent_window)


# opening a website to new window
driver.switch_to.new_window('window')
sleep(5)
driver.get("https://www.cricbuzz.com")