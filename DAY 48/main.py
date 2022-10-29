from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
#
#
# portal = driver.find_element(By.LINK_TEXT, 'Wikipedia')
# # portal.click()
#
# search = driver.find_element(By.NAME, 'search')
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)


# driver.close()

##challenges
# driver.get("https://secure-retreat-92358.herokuapp.com/")
# fName = driver.find_element(By.NAME, 'fName')
# fName.send_keys('Oluwatobiloba')
#
# lName = driver.find_element(By.NAME, 'lName')
# lName.send_keys('Hunkuten')
#
# emailAdd = driver.find_element(By.NAME, 'email')
# emailAdd.send_keys('thankyouangie@grateful.com')
#
# button = driver.find_element(By.CSS_SELECTOR, 'form button')
# button.send_keys(Keys.ENTER)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.XPATH, r"//*[@id='cookie']")
money = driver.find_element(By.XPATH, r"//*[@id='money']")
cps = driver.find_element(By.CSS_SELECTOR, "#cps")


def buyItem():
    storeItems = driver.find_elements(By.CSS_SELECTOR, "#store div:not(.grayed) b")
    storePrices = [float((item.text.split()[2]).replace(",", ".")) for item in storeItems]
    maxIndex = storePrices.index(max(storePrices))
    storeItems[maxIndex].click()


buyInterval = time.time() + 5
measureInterval = time.time() + 60 * 5

while measureInterval >= time.time():
    cookie.click()
    if time.time() >= buyInterval:
        buyItem()
        buyInterval = time.time() + 5

print(cps.text)