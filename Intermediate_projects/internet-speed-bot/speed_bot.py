from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver_path = "C:\operadriver.exe"
        self.driver = webdriver.Chrome(self.driver_path)
        self.down = ""
        self.up = ""

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go = self.driver.find_element(by=By.CLASS_NAME, value="start-text")
        go.click()
        time.sleep(50)
        self.down = self.driver.find_element(by=By.CSS_SELECTOR, value=".result-item-download .download-speed")
        self.down = self.down.text
        print(f"down: {self.down}")
        self.up = self.driver.find_element(by=By.CSS_SELECTOR, value=".result-item-upload .upload-speed")
        self.up = self.up.text
        print(f"upload: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        time.sleep(5)
        login = self.driver.find_element(by=By.TAG_NAME, value="input")
        login.send_keys("TWITTER ID")
        conti = self.driver.find_element(by=By.XPATH,
                                         value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div')
        conti.click()
        time.sleep(2)
        pas = self.driver.find_element(by=By.NAME, value="password")
        pas.send_keys("TWITTER PASSWORD")
        log = self.driver.find_element(by=By.XPATH,
                                       value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        log.click()
        time.sleep(5)
        tweet = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        tweet.send_keys(
            f"Hey Internet Provider, why is my internet speed {self.down}/down and {self.up}/up. when I pay for 150/down and 150/up")
        send = self.driver.find_element(by=By.XPATH,
                                        value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        send.click()
