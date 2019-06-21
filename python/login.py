from selenium import webdriver
import time

readr_home = "https://www.readr.tw/"
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver") # Use Chrome
driver.get(readr_home)

# 進入登入畫面
login_button = driver.find_element_by_xpath('//*[@id="app"]/header/div/nav[1]/div/div/p')
login_button.click()

# 輸入帳號
account_field = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div[3]/div[2]/div[1]/input')
account_field.send_keys("yychen@mirrormedia.mg")

# 輸入密碼
password_field = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div[3]/div[2]/div[2]/input')
password_field.send_keys("mirrormedia")

# 按下登入按鈕
login_trigger = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[3]/div[3]/div[2]/div[4]')
login_trigger.click()

time.sleep(5)

driver.quit()