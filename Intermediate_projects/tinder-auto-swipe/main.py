from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_path = "C:\operadriver.exe"

driver = webdriver.Chrome(driver_path)
driver.get("https://tinder.com/")
time.sleep(3)

login = driver.find_element(by=By.LINK_TEXT, value='Log in')
login.click()
time.sleep(2)
cookie = driver.find_element(by=By.XPATH, value='//*[@id="c849239686"]/div/div[2]/div/div/div[1]/div[1]/button')
cookie.click()
google = driver.find_element(by=By.XPATH, value='//*[@id="c-879141390"]/div/div/div[1]/div/div/div[3]/span/div[3]/button')
google.click()
time.sleep(20)
number = driver.find_element(by=By.XPATH, value='//*[@id="c-879141390"]/div/div/div[1]/div/div[2]/div/input')
number.send_keys("your number")
time.sleep(8)
submit = driver.find_element(by=By.XPATH, value='//*[@id="c-879141390"]/div/div/div[1]/div/button')
submit.click()
time.sleep(10)
conti = driver.find_element(by=By.XPATH, value='//*[@id="c-879141390"]/div/div/div[1]/div/button')
conti.click()
for clic in range(101):
    like = driver.find_element(by=By.XPATH,value='//*[@id="c849239686"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span/svg/path')
    like.click()
    time.sleep(1)