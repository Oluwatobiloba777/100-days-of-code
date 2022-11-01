from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


FACEBOOK = "YOUR FACEBOOK EMAIL"
FACEBOOK_PASSWORD = "FACEBOOK PASSWORD"

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.tinder.com")


sleep(3)
loginButton = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
loginButton.click()

sleep(3)
facebookLogin = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebookLogin.click()


#for the base windowsa
sleep(2)
baseWindow = driver.window_handles[0]
facebookLoginWindow = driver.window_handles[1]
driver.switch_to.window(facebookLoginWindow)
print(driver.title)

#
email = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH, '//*[@id="pass"]')
email.send_keys(FACEBOOK)
password.send_keys(FACEBOOK_PASSWORD)
password.send_keys(Keys.ENTER)

#Switch back to Tinder window
driver.switch_to.window(baseWindow)
print(driver.title)

#delay for 4seconds

#it allows location
allowLocationButton = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allowLocationButton.click()

#it disallows notifications
notificationButton = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notificationButton.click()

#it allowss cookies
cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#likes for 100 per day
for n in range(100):

    #delay for a second
    sleep(1)

    try:
        print("called")
        likeButton = driver.find_element(By.XPATH,
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        likeButton.click()

    #it will catch if there is match
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        #it will retry after 2seconds
        except NoSuchElementException:
            sleep(2)

driver.quit()