from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
sleep(2)
checkbox = driver.find_element(By.LINK_TEXT, "Checkboxes")
print(checkbox.text)
drag_drop = driver.find_element(By.PARTIAL_LINK_TEXT, "Drag")
print(drag_drop.text)
li_elements = driver.find_elements(By.TAG_NAME, "li")
print(len(li_elements))
driver.get("https://the-internet.herokuapp.com/tables")
sleep(2)
website = "//table[@id='table1']//td[text()='jdoe@hotmail.com']/following-sibling::td[2]"
website = driver.find_element(By.XPATH, website)
print("Website for jdoe@hotmail.com:", website.text)
delete = "//table[@id='table1']//td[text()='Bach']/following-sibling::td/a[text()='delete']"
delete_link = driver.find_element(By.XPATH, delete)
print("Delete link for Bach found:", delete_link.text)
second_table = driver.find_element(By.XPATH, "(//table)[2]")
print("Second table found:", second_table.tag_name)
cell_xpath = "//table[@id='table2']//td[text()='$100.00']"
cell = driver.find_element(By.XPATH, cell_xpath)
parent_row = cell.find_element(By.XPATH, "./ancestor::tr")
print("Row containing $100.00:", parent_row.text)
driver.quit()