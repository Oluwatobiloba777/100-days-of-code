from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "YOUR TWITTER EMAIL"
TWITTER_PASSWORD = "TWITTER PASSWORD"
TWITTER_URL = "https://twitter.com/home"
lEN_CHAR = 280

chrome_driver_path = "C:\Development\chromedriver.exe"
SERVICE = Service(chrome_driver_path)
DRIVER = webdriver.Chrome(service=SERVICE)


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = DRIVER
        self.down = 0
        self.up = 0

    def getInternetSpeed(self):
        self.driver.get('https://fast.com/')
        time.sleep(40)

        showMoreInfo = self.driver.find_element(By.ID, 'show-more-details-link')
        showMoreInfo.click()

        downSpeed = self.driver.find_element(By.ID, 'speed-value')
        print(downSpeed.text)

        upSpeed = self.driver.find_element(By.ID, 'upload-value')
        print(upSpeed.text)

    def tweetAtProvider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(3)
        # Login
        username = self.driver.find_element(By.NAME, 'text')
        username.send_keys(TWITTER_EMAIL)
        username.send_keys(Keys.ENTER)
        time.sleep(3)

        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(3)

        # Compose and send Tweet
        message = f"Test tweet for DAY51 of #100DaysofPython Twitter bot: Hey Internet Provider! " \
                  f"Why is my internet speed {self.down} down/{self.up} up when I pay " \
                  f"for {PROMISED_DOWN} down/{PROMISED_UP} up?"
        compose_tweet = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        compose_tweet.send_keys(message)
        time.sleep(2)
        send_tweet = self.driver.find_element(By.XPATH, '//*[text()="Tweet"]')
        send_tweet.click()


twitterBot = InternetSpeedTwitterBot()
twitterBot.getInternetSpeed()
twitterBot.tweetAtProvider()
