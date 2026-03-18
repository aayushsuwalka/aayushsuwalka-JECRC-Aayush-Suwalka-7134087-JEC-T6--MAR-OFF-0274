from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")
sleep(2)
driver.execute_script("document.body.classList.remove('modal-open');")
driver.execute_script("document.querySelectorAll('iframe').forEach(el => el.remove());")
driver.find_element(By.ID, "firstName").send_keys("Aayush")
driver.find_element(By.ID, "lastName").send_keys("Suwalka")
driver.find_element(By.ID, "userEmail").send_keys("aayush.suwalka08@gmail.com")
driver.find_element(By.XPATH, "//label[text()='Male']").click()
driver.find_element(By.ID, "userNumber").send_keys("6350032742")
subjects = driver.find_element(By.ID, "subjectsInput")
subjects.send_keys("Maths")
subjects.send_keys(Keys.ENTER)


driver.find_element(By.XPATH, "//label[text()='Sports']").click()
driver.find_element(By.XPATH, "//label[text()='Music']").click()
driver.find_element(By.ID, "currentAddress").send_keys("B-325, Subhash Nagar Bhilwara ")
state = driver.find_element(By.ID, "react-select-3-input")
state.send_keys("NCR")
state.send_keys(Keys.ENTER)
city = driver.find_element(By.ID, "react-select-4-input")
city.send_keys("Bhilwara")
city.send_keys(Keys.ENTER)

sleep(2)
driver.find_element(By.ID, "submit").click()

sleep(3)
try:
    modal_title = driver.find_element(By.ID, "example-modal-sizes-title-lg")
    print("Form submitted successfully:", modal_title.text)
except:
    print("Submission might have failed")
sleep(5)
driver.quit()