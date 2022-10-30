from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#linkedin email access
EMAIL_ADD = "YOUR EMAIL ADDRESS"
PASSWORD = "YOUR PASSWORD"
PHONE_NUMBER = "YOUR PHONE NUMBER"

chrome_driver_path = "YOUR CHROME DRIVER PATH"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("LINKEDIN URL")

signIn = driver.find_element(By.LINK_TEXT, 'Sign in')
signIn.click()

#SIGN IN
time.sleep(2)

username = driver.find_element(By.ID, 'username')
username.send_keys(EMAIL_ADD)
password = driver.find_element(By.ID, 'password')
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

#APPLY
time.sleep(3)
apply = driver.find_element(By.CSS_SELECTOR, '.jobs-s-apply button')
apply.click()

#SUBMIT APPLICATION

submit = driver.find_element(By.CSS_SELECTOR, 'footer button')
submit.click()
