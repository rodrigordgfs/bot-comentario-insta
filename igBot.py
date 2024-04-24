from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import json
import time
import random


class InstagramBot:
    WAIT_LONG_TIME = 30
    WAIT_SHORT_TIME = 15

    def __init__(self, username, password):
        self.options = webdriver.FirefoxOptions()
        self.options.binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.file_name = os.environ.get("FILE_NAME")
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(
            executable_path='geckodriver.exe',
            options=self.options
        )
        self.locators = {
            'username': (By.XPATH, "//input[@name='username']"),
            'password': (By.XPATH, "//input[@name='password']")
        }
        self.comments_count = 0

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

    def increase_comments_count(self, comment):
        self.comments_count += 1
        print("{} - {} ".format(self.comments_count, comment))

    def comment_photo(self, url):
        time.sleep(self.WAIT_LONG_TIME)
        driver = self.driver
        driver.get(url)

        with open(self.file_name, "r") as file:
            user_file = json.load(file)
            comment_list = random.sample(user_file, len(user_file))

        try:
            for comment in comment_list:
                comment_button = WebDriverWait(driver, self.WAIT_LONG_TIME).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "xs3hnx8"))
                )
                comment_button.click()

                comment_input = WebDriverWait(driver, self.WAIT_LONG_TIME).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "xs3hnx8"))
                )
                comment_input.clear()

                for letter in comment:
                    comment_input.send_keys(letter)
                    time.sleep(random.randint(1, 2) / 30)

                driver.find_element(
                    By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/div[2]/div").click()

                self.increase_comments_count(comment)

                time.sleep(15)
                comment_input.clear()

        except Exception as e:
            print("Error commenting on photo:", e)


if __name__ == "__main__":
    bot = InstagramBot(os.environ.get("USERNAME"), os.environ.get("PASSWORD"))
    bot.login()
    bot.comment_photo(os.environ.get('POST_URL'))
