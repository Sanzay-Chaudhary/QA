from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 15)

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

driver.find_element(By.ID, "username").send_keys("tomsmith")

driver.find_element(By.ID, "password").send_keys("WrongPassword!")

driver.find_element(By.CSS_SELECTOR, "Button[type='submit']").click()

error_message = wait.until(
    EC.presence_of_element_located((By.ID, "flash"))
)

assert "Your password is invalid" in error_message.text
print("Test failed: Login failed as expected")


driver.quit()
