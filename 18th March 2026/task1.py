from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.lenskart.com/")
driver.maximize_window()
sleep(5)
sunglass = driver.find_element(By.ID, 'lrd5')
sunglass.click()
sleep(3)
sortby = driver.find_element(By.ID, 'sortByDropdown')
selectSortBy = Select(sortby)
selectSortBy.select_by_value('saving')
sleep(5)
firstglass = driver.find_element(By.XPATH, "(//div[@class='sc-23b7d3eb-6 hYdmOJ']/div/following-sibling::p[@class='sc-23b7d3eb-2 dQrJBg'])[1]")
print(firstglass.text)

