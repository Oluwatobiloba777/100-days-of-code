from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException,NoSuchElementException
import time


SIMILAR_ACCOUNT = "NAME OF ACCOUNT WHO HAS MANY FOLLOWERS"
USERNAME = "INSTAGRAM USERNAME"
PASSWORD = "INSTAGRAM PASSWORD"

chrome_driver_path = "YOUR CHROME DRIVER PATH"
DRIVER = webdriver.Chrome(executable_path=chrome_driver_path)


class InstaFollower:
    def __init__(self):
        self.driver = DRIVER

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        #login

        username = self.driver.find_element(By.NAME, 'username')
        username.send_keys(USERNAME)
        time.sleep(1)

        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(2)

    def findFollowers(self):
        self.driver.get("https://www.instagram.com/chefsteps/")

        followers = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'follower')
        followers.click()

        following = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')

        for a in range(20):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", following)
            time.sleep(2)

    def follow(self):
        follows = self.driver.find_element(By.CSS_SELECTOR, '.isgrP button')
        for folow in follows:
            try:
                folow.click()
            except:
                cancel = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel.click()
                time.sleep(3)

                self.driver.quit()


followerBot = InstaFollower()
followerBot.login()
followerBot.findFollowers()
followerBot.follow()