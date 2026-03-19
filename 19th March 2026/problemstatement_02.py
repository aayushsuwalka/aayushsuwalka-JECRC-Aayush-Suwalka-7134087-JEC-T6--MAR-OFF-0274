from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get('https://qavbox.github.io/demo/signup/')
wait = WebDriverWait(driver, 10)
full_name = wait.until(EC.presence_of_element_located((By.ID, 'username')))
full_name.click()
full_name.send_keys("Aayush Suwalka")
email = wait.until(EC.presence_of_element_located((By.ID, 'email')))
email.click()
email.send_keys("aayush.suwalka08@gmail.com")
telephone = wait.until(EC.presence_of_element_located((By.ID, 'tel')))
telephone.click()
telephone.send_keys("6350032742")
# faxNo = wait.until(EC.presence_of_element_located((By.ID, 'fax')))
# faxNo.click()
# faxNo.send_keys("6350032742")
choose_file = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
choose_file.send_keys(r"C:\Users\aayus_ucf5jw3\OneDrive\Pictures\Screenshots 1\Screenshot 2026-01-29 120949.png")
gen = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@name='sgender']")))
gender = Select(gen)
gender.select_by_value("male")
experience = wait.until(EC.presence_of_all_elements_located((By.XPATH, "(//input[@type='radio'])")))
experience[4].click()
skills = wait.until(EC.presence_of_all_elements_located((By.ID, 'ip')))

skills[2].click()
tools = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@id='tools']")))
t = Select(tools)
t.select_by_value("selenium")
submit = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='submit']")))
submit.click()
sleep(2)
driver.quit()


