from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver") # Use Chrome
driver.get("https://www.readr.tw/")

print(driver.current_url)

time.sleep(5)

driver.quit()