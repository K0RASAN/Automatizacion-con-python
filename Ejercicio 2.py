from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

btnForm = '//*[@id="app"]/div/div/div[2]/div/div[2]/div'
btnElements = '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]'
btnWebTables = '//*[@id="item-3"]'

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()
driver.get("https://demoqa.com/")


clickbtnForm = wait.until(EC.visibility_of_element_located((By.XPATH, btnForm))) 
driver.execute_script("arguments[0].scrollIntoView(true);", clickbtnForm)
clickbtnForm.click()
time.sleep(1)

clickbtnElements = wait.until(EC.visibility_of_element_located((By.XPATH, btnElements))) 
driver.execute_script("arguments[0].scrollIntoView(true);", clickbtnElements)
clickbtnElements.click()
time.sleep(1)

clickbtnWebTables = wait.until(EC.visibility_of_element_located((By.XPATH, btnWebTables))) 
driver.execute_script("arguments[0].scrollIntoView(true);", clickbtnWebTables)
clickbtnWebTables.click()

driver.find_element(By.ID, "addNewRecordButton").click()
time.sleep(1)

driver.find_element(By.ID, "firstName").send_keys("Marjhory")
driver.find_element(By.ID, "lastName").send_keys("Alexander")
driver.find_element(By.ID, "userEmail").send_keys("marjhory@example.com")
driver.find_element(By.ID, "age").send_keys("21")
driver.find_element(By.ID, "salary").send_keys("50000")
driver.find_element(By.ID, "department").send_keys("Automation")
driver.find_element(By.ID, "submit").click()
time.sleep(1)

search_box = driver.find_element(By.ID, "searchBox")
search_box.send_keys("Marjhory")
time.sleep(1)

edit_button = driver.find_element(By.CSS_SELECTOR, "span[title='Edit']")
driver.execute_script("arguments[0].scrollIntoView(true);", edit_button)
edit_button.click()
time.sleep(1)

driver.find_element(By.ID, "age").clear()
driver.find_element(By.ID, "age").send_keys("22")
driver.find_element(By.ID, "salary").clear()
driver.find_element(By.ID, "salary").send_keys("60000")
driver.find_element(By.ID, "department").clear()
driver.find_element(By.ID, "department").send_keys("Quality Assurance")
driver.find_element(By.ID, "submit").click()
time.sleep(1)

search_box.clear()
search_box.send_keys("Marjhory")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "span[title='Delete']").click()



time.sleep(10)
