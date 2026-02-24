from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#step 1: set up the browser
driver = webdriver.Chrome()
driver.maximize_window()

#step 2: open login page
driver.get("https://the-internet.herokuapp.com/login")

#find username field and enter text
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

#find password field and enter text
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")
# password.send_keys("WrongPassword123")

#click login button
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

time.sleep(2)

#validate login successful
success_message = driver.find_element(By.ID, "flash").text

if "You logged into a secure area!" in success_message:
    print("Login successful!")

else:
    print("Login test failed!")

time.sleep(3)
driver.quit()
