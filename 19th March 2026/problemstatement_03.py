# TAsk 3
# 1. navigate to amazon
# 2. search a product through send_keys
# BUT dont click on search or keys.enter
# 3. Wait for the suggestions to appear
# 4. Click on 4th suggestion
# 5. Click on Sort By and click on newest
# 6. Click on free shipping check box
# 7. wait for first product and return me the name=price
# (without using inner text)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get('https://www.amazon.in/')
driver.maximize_window()
wait = WebDriverWait(driver, 10)
search = wait.until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
search.send_keys('laptop')
suggestion = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@role='row'])[4]")))
suggestion.click()
sort_dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@id='a-autoid-0-announce']")))
sort_dropdown.click()
newest_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Newest Arrivals')]")))
newest_option.click()
free_delivery = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Free Delivery')]")))
free_delivery.click()
product = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@data-component-type='s-search-result'])[1]")))
name = product.find_element(By.XPATH, ".//h2//span").get_attribute("innerHTML")
price_elements = product.find_elements(By.XPATH, ".//span[contains(@class,'a-price')]//span[@class='a-price-whole']")
if price_elements:
    price = price_elements[0].get_attribute("innerHTML")
else:
    price = "Price not available"
print(f"Product Name: {name}")
print(f"Price: ₹{price}")