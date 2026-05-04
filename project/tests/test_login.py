from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start browser
driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")

driver.maximize_window()

wait = WebDriverWait(driver, 15)

print("Website opened")

# Enter username
username = wait.until(
    EC.presence_of_element_located((By.ID, "username"))
)

username.send_keys("tomsmith")

# Enter password
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

# Click login button
login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_btn.click()

print("Login button clicked")

driver.quit()