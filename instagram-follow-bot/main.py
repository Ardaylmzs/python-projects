import os
from time import sleep
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

load_dotenv()

class FollowersBot:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
        self.webdriver = webdriver.Chrome(options=self.options)
        self.webdriver.get("https://instagram.com")
        sleep(5)

    def login(self):
        username = self.webdriver.find_element(By.XPATH, value='//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        username.send_keys(os.environ.get("INSTAGRAM_USERNAME"))
        password = self.webdriver.find_element(By.XPATH , value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        password.send_keys(os.environ.get("PASSWORD"))
        login_button = self.webdriver.find_element(By.XPATH , value='//*[@id="loginForm"]/div[1]/div[3]/button')
        login_button.click()
        sleep(5)

    def find_followers(self):
        save_login_prompt = self.webdriver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()
            sleep(10)
        try:
            target_account = os.environ.get("TARGET_ACCOUNT")
            self.webdriver.get(f"https://www.instagram.com/{target_account}/followers/")
            sleep(10)
            followers = self.webdriver.find_element(By.XPATH, value='//a[contains(@href, "/433/followers/")]')
            followers.click()
            sleep(5)
        except NoSuchElementException:
            print("we encounter a problem :(")

    def following(self):
        users = self.webdriver.find_elements(By.XPATH, value='//div[contains(@class,"x1qnrgzn x1cek8b2 xb10e19 x19rwo8q x1lliihq x193iq5w xh8yej3")]')[:5]
        for user in users:
            follow = self.webdriver.find_element(By.XPATH , value='//button[contains(@class," _aswp _aswr _aswu _asw_ _asx2")]')
            follow.click()
            print(f"Following {user.text}")
            print("the process is completed")

followers_bot = FollowersBot()
followers_bot.login()
followers_bot.find_followers()
followers_bot.following()


