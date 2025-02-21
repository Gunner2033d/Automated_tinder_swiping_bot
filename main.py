import time

from dotenv import load_dotenv
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
load_dotenv()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://tinder.com/")
time.sleep(2)
login_button = driver.find_element(By.XPATH,"//div[text()='Log in']")
login_button.click()
time.sleep(3)
try:
    option_button = driver.find_element(By.XPATH,"//button[text()='More Options']")
    option_button.click()
except NoSuchElementException:
    print("No Option button")
finally:
    facebook_login = driver.find_element(By.XPATH,"//div[text()='Log in with Facebook']")
    facebook_login.click()

#Facebook Login Inputs
time.sleep(3)
windows = driver.window_handles # Get the first iframe
base_window = windows[0]
fb_login_window = windows[1]   #Switch to it
driver.switch_to.window(fb_login_window)
time.sleep(3)
email = driver.find_element(By.XPATH, "//input[@id='email']")
time.sleep(1)
email.send_keys(os.getenv("EMAIL"))
password = driver.find_element(By.XPATH, "//input[@id='pass']")
time.sleep(1)
password.send_keys(os.getenv("PASSWORD"),Keys.ENTER)
time.sleep(2)
try:
    continue_button = driver.find_element(By.XPATH,"//div[@aria-label='Continue as Rohan']")
    continue_button.click()
    time.sleep(2)
except NoSuchElementException:
    print("No Option")
time.sleep(3)
driver.switch_to.window(base_window)
time.sleep(2)
button = driver.find_element(By.XPATH, '//button[@aria-label="Allow"]')
button.click()
time.sleep(2)
decline = driver.find_element(By.XPATH,value="//button[@data-testid='decline']")
decline.click()
cookie_accept = driver.find_element(By.CLASS_NAME,value="c1p6lbu0")
cookie_accept.click()

time.sleep(5)
for i in range(25):
    try:
        time.sleep(1)
        like_button = driver.find_element(By.XPATH,value='//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[4]')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)
    except NoSuchElementException:
        try:
            like_button = driver.find_element(By.XPATH,
                                             value='//*[@id="main-content"]/div[1]/div/div/div/div[1]/div/div/div[5]/div/div[4]')
            like_button.click()
        # For "Add Tinder to your Home Screen" pop-up
        except ElementClickInterceptedException:
            not_interested_button = driver.find_element(By.XPATH,value="//button[.//div[contains(text(), 'Not interested')]]")

            not_interested_button.click()




