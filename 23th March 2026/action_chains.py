from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Drag and Drop

# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/drag_and_drop")
# driver.maximize_window()
# sleep(3)
# action = ActionChains(driver)
# ori_ele = driver.find_element(By.ID, 'column-a')
# tar_ele = driver.find_element(By.ID, 'column-b')
# action.drag_and_drop(ori_ele, tar_ele).perform()
# sleep(3)


# Mouse Hover

# driver = webdriver.Chrome()
# driver.get("https://supertails.com")
# driver.maximize_window()
# sleep(3)
# action = ActionChains(driver)
# doggo = driver.find_element(By.XPATH, '(//span[contains(text(),"Dog")])[1]')
# sleep(3)
# action.move_to_element(doggo).perform()
# sleep(4)


# Scrolling to element by using Mouse Actions

# driver = webdriver.Chrome()
# driver.get("https://supertails.com")
# driver.maximize_window()
# sleep(3)
# action = ActionChains(driver)
# catto = driver.find_element(By.XPATH, '//div[@data-ganame="Breed 5"]')
# sleep(3)
# action.scroll_to_element(catto).perform()
# sleep(4)
# action.scroll_by_amount(delta_x=0, delta_y=-1500).perform()
# sleep(4)

# KeyBoard Actions
# driver = webdriver.Chrome()
# driver.get("https://supertails.com")
# driver.maximize_window()
# sleep(3)
# action = ActionChains(driver)
# # action.send_keys(Keys.PAGE_DOWN)
# # sleep(3)
# # action.send_keys(Keys.PAGE_UP)
# # sleep(3)
# action.key_down(Keys.CONTROL).send_keys('a').perform()
# sleep(3)
# action.key_up(Keys.CONTROL).perform()
# sleep(3)
# action.key_down(Keys.CONTROL).send_keys('c').perform()
# sleep(3)
# action.key_up(Keys.CONTROL).perform()
# sleep(3)

# Coping and pasting for address fields
# driver = webdriver.Chrome()
# driver.get(r"C:\Users\aayus_ucf5jw3\OneDrive\Desktop\Project_Selenium\23th March 2026\index.html")
# driver.maximize_window()
# action = ActionChains(driver)
# present = driver.find_element(By.ID, "presentAddress")
# permanent = driver.find_element(By.ID, "permanentAddress")
# present.send_keys("JECRC, JAIPUR, RJ")
# sleep(3)
# present.click()
# action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
# sleep(1)
# action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
# permanent.click()
# sleep(3)
# action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
# sleep(5)

# Password Visibility
driver = webdriver.Chrome()
driver.get(r"C:\Users\aayus_ucf5jw3\OneDrive\Desktop\Project_Selenium\23th March 2026\index1.html")
driver.maximize_window()
action = ActionChains(driver)
driver.find_element(By.ID, 'password').send_keys("Aayush")
sleep(3)
show_pass = driver.find_element(By.ID, 'eyeBtn')
action.click_and_hold(show_pass).perform()
sleep(3)
action.release()

