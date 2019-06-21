from selenium import webdriver
import time

readr_home = "https://www.readr.tw/"
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver') # Use Chrome
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

# 選取所有專題
project_elems = driver.find_elements_by_xpath('//div[@class="series-list home__list"]/a')
time.sleep(1)

# 記錄目前視窗
base_window = driver.current_window_handle
for project_elem in project_elems:

	# 開新視窗，並把焦點移到新視窗
	project_elem.click()
	for window in driver.window_handles:
		if window != base_window:
			driver.switch_to_window(window)
	
	content_text = driver.find_element_by_xpath('//p[@class="app-content-area"]')
	print(content_text.text)

	time.sleep(1)
	
	# 關閉視窗，把焦點移回原視窗
	driver.close()
	driver.switch_to_window(base_window)

driver.quit()