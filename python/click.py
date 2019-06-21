from selenium import webdriver
import time

readr_home = "https://www.readr.tw/"
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver") # Use Chrome
driver.get(readr_home)

# 進入登入畫面
login_button = driver.find_element_by_xpath('//*[@id="app"]/header/div/nav[1]/div/div/p')
login_button.click()

time.sleep(5)

driver.quit()