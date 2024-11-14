from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


btnForm = '//*[@id="app"]/div/div/div[2]/div/div[2]/div'
btnPracticeForm = '//*[@id="app"]/div/div/div/div[1]/div/div/div[2]/div'

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()
driver.get("https://demoqa.com/")

clickbtnForm = wait.until(EC.visibility_of_element_located((By.XPATH, btnForm))) 
clickbtnForm.click()

clickbtnPracticeForm = wait.until(EC.visibility_of_element_located((By.XPATH, btnPracticeForm))) 
clickbtnPracticeForm.click()

wait.until(EC.visibility_of_element_located((By.ID, "firstName")))
driver.find_element(By.ID, "firstName").send_keys("Marjhory Alexander")
driver.find_element(By.ID, "lastName").send_keys("De Los Santos Asencio")
driver.find_element(By.ID, "userEmail").send_keys("marjhory@example.com")
driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']").click()  
driver.find_element(By.ID, "userNumber").send_keys("1234567890")

driver.find_element(By.ID, "dateOfBirthInput").click()
time.sleep(1) 
driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("2003")
driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("February")
driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--003").click() 

driver.find_element(By.ID, "subjectsInput").send_keys("Maths")
driver.find_element(By.ID, "subjectsInput").send_keys(Keys.RETURN)
driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']").click()

driver.find_element(By.ID, "uploadPicture").send_keys("C:/Users/Koray/Automatizando con Py/foto.jpg")

driver.find_element(By.ID, "currentAddress").send_keys("avenida siempre viva 214")

submit_button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
submit_button.click()

time.sleep(10)