from selenium import webdriver
browser = "edge"

if browser == "chrome":
    driver = webdriver.Chrome()

elif browser == "firefox":
    driver = webdriver.Firefox()

elif browser == "edge":
    driver = webdriver.Edge()

driver.get("https://www.google.com")

driver.quit()

