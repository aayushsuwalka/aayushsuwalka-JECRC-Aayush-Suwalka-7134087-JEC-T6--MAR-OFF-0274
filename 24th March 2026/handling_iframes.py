from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

# single frame
# frame = driver.find_element(By.ID, "singleframe")
# driver.switch_to.frame(frame)
# sleep(2)
# driver.find_element(By.XPATH, '//input[@type="text"]').send_keys("123")
# sleep(2)


# nested frames
driver.find_element(By.XPATH, '//a[text()="Iframe with in an Iframe"]').click()
nested_iframe = driver.find_element(By.XPATH, '//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(nested_iframe)

inner_iframe = driver.find_element(By.XPATH, '//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(inner_iframe)

driver.find_element(By.XPATH, '//input[@type="text"]').send_keys("123")
sleep(5)
driver.switch_to.parent_frame() #switch to parent frame
driver.switch_to.default_content() # switch to default page
