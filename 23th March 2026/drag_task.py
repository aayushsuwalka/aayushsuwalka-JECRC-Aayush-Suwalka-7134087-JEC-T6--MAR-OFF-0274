from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/droppable")
# driver.maximize_window()
# sleep(3)
# action = ActionChains(driver)
# ori = driver.find_element(By.ID, 'draggable')
# tar = driver.find_element(By.ID, 'droppable')
# action.drag_and_drop(ori, tar).perform()
# sleep(3)
# act_text = tar.text
# exp_text = "Dropped!"
# assert act_text == exp_text , f"Test Failed {exp_text} expected, but received {act_text}"
# print("Test Passed")

# task 2
driver = webdriver.Chrome()
driver.get("https://demoqa.com/droppable")
driver.maximize_window()
sleep(3)
action = ActionChains(driver)
click_pre = driver.find_element(By.ID, "droppableExample-tab-preventPropogation").click()

sleep(3)
ori = driver.find_element(By.ID, 'draggable')
tar = driver.find_element(By.ID, 'droppable')
action.drag_and_drop(ori, tar).perform()
# act_text = tar.text
# exp_text = "Dropped!"
# assert act_text == exp_text , f"Test Failed {exp_text} expected, but received {act_text}"
# print("Test Passed")

