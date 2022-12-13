from selenium import webdriver
import pyautogui
import time

GAME_URL = 'https://elgoog.im/t-rex/'
DRIVER_PATH = 'YOUR PATH TO THE SELENIUM CHROMEDRIVER'


driver = webdriver.Chrome(executable_path=DRIVER_PATH)
dinosaur_site = driver.get(url=GAME_URL)

time.sleep(5)
pyautogui.press('up')

game_on = True
while game_on:
      image = pyautogui.screenshot()
      screen = image.getpixel((174, 355))
      x1 = image.getpixel((330, 450))
      x2 = image.getpixel((360, 450))
      x3 = image.getpixel((320, 450))
      x4 = image.getpixel((400, 450))
      if screen[0] == 247:
            if x1[0] != 247 or x2[0] != 247 or x3[0] != 247 or x4[0] != 247:
                  pyautogui.press('up')
                  time.sleep(0.0001)