from selenium import webdriver
driver = webdriver.Chrome("C:/Atish Documents/chromedriver_win32/chromedriver.exe")

driver.get("http://www.facebook.com")
driver.maximize_window()
username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
submit = driver.find_element_by_name("login")
username.send_keys("you@email.com")
password.send_keys("yourpassword")

submit.click()

