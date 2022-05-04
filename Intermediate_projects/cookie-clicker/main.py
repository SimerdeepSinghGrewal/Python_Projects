from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver_path = "C:\chromedriver.exe"

driver = webdriver.Chrome(driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

click_cookie = driver.find_element(by=By.CSS_SELECTOR, value="#bigCookie")
five = time.time() + 19000
gap = time.time() + 300
yes = True
time.sleep(30)
while yes:
    time_out = time.time()
    click_cookie.click()
    # if time_out > gap:
    #     time.sleep(40)
    #     gap = time.time() + 300
    if time_out > five:
        yes = False
