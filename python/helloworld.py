from selenium import webdriver
import time

readr_home = "https://www.readr.tw/"
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver") # Use Chrome
driver.get(readr_home)

print(driver.current_url)

time.sleep(5)

driver.quit()