from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.opencart.com")

print("website open successfully")
driver.quit()