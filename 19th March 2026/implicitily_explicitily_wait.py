from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
# driver.get('https://abc.com')
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)
# loading_circle = wait.until(EC.invisibility_of_element_located((By.ID, 'preloader-animated_svg__svg3')))
# title_abc = driver.find_element(By.XPATH, '//span[text()="ABC SHOWS, SPECIALS & MORE"]')
#
# assert 'SPECIALS' in title_abc.text, 'the text not present'
# print('working fine')
# driver.quit()

# driver.get('https://demoqa.com/dynamic-properties')
# driver.maximize_window()
# wait = WebDriverWait(driver, 6)
# enable_before = driver.find_element(By.ID, 'enableAfter')
# print(enable_before.is_enabled())
# enable_btn = wait.until(EC.element_to_be_clickable(By.ID, 'enableAfter'))
#
# if enable_btn.is_enabled():
#     enable_btn.click()
#     print(enable_btn.text)
# visible_ele = wait.until(EC.visibility_of_element_located(By.ID, 'visibleAfter'))
# visible_ele.click()
#
# driver.quit()


driver.get("https://demo.mobiscroll.com/select/multiple-select")
driver.maximize_window()

multi_drop = driver.find_element(By.XPATH, '//select[@id="multiple-select-select"]')
select = Select(multi_drop)
if select.is_multiple():
    select.select_by_value("1")
    select.select_by_value("2")
    select.select_by_value("3")
sleep(5)
select.deselect_by_index(6)
select.deselect_all()
print(select.first_selected_option)
print(select.all_selected_options)
driver.quit()