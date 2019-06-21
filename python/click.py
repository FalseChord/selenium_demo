from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver") # Use Chrome
driver.get("https://www.readr.tw/")

# 進入登入畫面
login_button = driver.find_element_by_xpath('//*[@id="app"]/header/div/nav[1]/div/div/p')
login_button.click()

time.sleep(5)

driver.quit()