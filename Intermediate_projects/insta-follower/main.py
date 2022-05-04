from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = "C:\operadriver.exe"

driver = webdriver.Chrome(driver_path)
driver.get("https://www.instagram.com/")
time.sleep(4)
user = driver.find_elements(by=By.TAG_NAME, value='input')
user[0].send_keys("insta user id")
user[1].send_keys("password")
# password = driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/span')
# password.send_keys("pasword")
login = driver.find_elements(by=By.TAG_NAME, value='button')
login[1].click()
time.sleep(5)
login = driver.find_elements(by=By.TAG_NAME, value='button')
login[1].click()
time.sleep(5)
# login = driver.find_elements(by=By.TAG_NAME, value='button')
# print(login)
# time.sleep(5)
search = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys("search Query")
search.send_keys(Keys.ENTER)
search = driver.find_element(by=By.ID, value='f1fbc92cbf09cc8')
search.click()
time.sleep(4)
follow = driver.find_element(by=By.TAG_NAME, value="a")
follow.click()