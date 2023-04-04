from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import json
import time
import random


class InstagramBot:
    WAIT_LONG_TIME = 10
    WAIT_SHORT_TIME = 5

    def __init__(self, username, password):
        self.options = Options()
        self.options.binary_location = os.environ.get("FIREFOX_PATH")
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(
            executable_path=os.environ.get("GECKODRIVER_PATH"),
            options=self.options
        )
        self.locators = {
            'username': (By.XPATH, "//input[@name='username']"),
            'password': (By.XPATH, "//input[@name='password']")
        }

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")

        try:
            username_input = WebDriverWait(driver, self.WAIT_LONG_TIME).until(
                EC.presence_of_element_located(self.locators['username'])
            )
            password_input = driver.find_element(*self.locators['password'])

            username_input.clear()
            username_input.send_keys(self.username)
            password_input.clear()
            password_input.send_keys(self.password)

            password_input.submit()

        except Exception as e:
            print("Error logging in:", e)

    def comment_photo(self, url):
        time.sleep(self.WAIT_LONG_TIME)
        driver = self.driver
        driver.get(url)

        with open("users.json", "r") as file:
            user_file = json.load(file)
            comment_list = random.sample(user_file, len(user_file))

        try:
            for comment in comment_list:
                comment_button = WebDriverWait(driver, self.WAIT_LONG_TIME).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "x1i0vuye"))
                )
                comment_button.click()

                comment_input = WebDriverWait(driver, self.WAIT_LONG_TIME).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "x1i0vuye"))
                )
                comment_input.clear()
                
                for letter in comment:
                    comment_input.send_keys(letter)
                    time.sleep(random.randint(1, 5) / 30)

                actions = ActionChains(driver)
                actions.send_keys(Keys.ENTER)
                actions.perform()

                time.sleep(75)
                comment_input.clear()

        except Exception as e:
            print("Error commenting on photo:", e)


if __name__ == "__main__":
    bot = InstagramBot(os.environ.get("USERNAME"), os.environ.get("PASSWORD"))
    bot.login()
    bot.comment_photo(os.environ.get('POST_URL'))
