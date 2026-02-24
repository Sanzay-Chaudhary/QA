from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Set up the browser
driver = webdriver.Chrome()

# Step 2: Open website
driver.get("http://automationpractice.com")


# Step 3: Wait for 5 seconds so you can see it open
time.sleep(5)

# Step 4: Close browser
driver.quit()

print("Browser opened and closed successfully!")
