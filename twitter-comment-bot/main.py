import requests
import os
from time import sleep
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException,TimeoutException

load_dotenv()

 # USE YOUR WINDOWS USERNAME
CHROME_USER_DATA_DIR = fr"C:\Users\{os.environ.get("chrome_user")}\AppData\Local\Google\Chrome\User Data"
CHROME_PROFILE_DIRECTORY = "Default"
CHROMEDRIVER_PATH = r"C:\path\to\chromedriver.exe"

URL = os.environ.get("URL")
API_KEY = os.environ.get("API_KEY")

headers = {
    "x-api-key": os.environ.get("X_API_KEY"),
}
comment_time = datetime.now()
if comment_time.hour == 17 and comment_time.minute == 00:
    class Comment:
        def __init__(self, q_text):
            self.q_text = q_text
            response = requests.get(URL, headers=headers)
            self.joke = response.json()[0]["joke"]

        def response(self):
            return f"{self.q_text} ---> {self.joke}"

    q_texts = "hello everyone!! I am stupidBott and I have one bad joke for you :)"
    comment = Comment(q_texts)
    print(comment.response())

    def make_driver():
        options = Options()
        # <--ARRANGE WITH YOUR INFORMATION HERE
        options.add_argument(r"--user-data-dir=C:\ChromeProfile")
        options.add_argument("--profile-directory=.")
        # DECREASE BOT FEATURES + DevToolsActivePort fix
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--disable-gpu")
        options.add_argument("--start-maximized")
        # WITH ChromeDriver Manager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    drivers = make_driver()
    drivers.get("https://twitter.com/login")
    sleep(5)
    iframes = drivers.find_elements(By.TAG_NAME, value="iframe")
    print("Iframe counts:", len(iframes))


    if len(iframes) > 0:
        drivers.switch_to.frame(iframes[0])
    else:
        print("there is no iframes ,keep going!")
    try:
        sign_in_btn = drivers.find_element(By.XPATH, value='//*[@id="container-div"]/div/div[2]/span[1]')
        sign_in_btn.click()
    except NoSuchElementException:
        print("continue!!")

    x_window = drivers.window_handles[0]
    window_ggl = drivers.window_handles[1]
    try:
        drivers.switch_to.window(window_ggl)
        try:
            sleep(7)
            ggl_email = drivers.find_element(By.CSS_SELECTOR, value='.Xb9hP input')
            ggl_email.send_keys(os.environ.get("GGL_EMAIL"))
            sleep(3)
            next_btn = drivers.find_element(By.XPATH, value='//*[@id="identifierNext"]/div/button/span')
            next_btn.click()
            sleep(3)
            ggl_password = drivers.find_element(By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input')
            ggl_password.send_keys(os.environ.get("GGL_PASSWORD"))
            sleep(2)
            next_btn2 = drivers.find_element(By.XPATH , value='//*[@id="passwordNext"]/div/button')
            next_btn2.click()
            try:
                sleep(2)
                continue_btn = drivers.find_element(By.XPATH, value='//*[@id="yDmH0d"]/c-wiz/main/div[3]/div/div/div[2]/div/div/button/span')
                continue_btn.click()
                sleep(2)
            except TimeoutException:
                pass
        except TimeoutException:
            print("don't loading login page! , comment section is beginning!!")

    except NoSuchElementException:
        print("don't loading login page! , comment section is beginning!!,")

    drivers.switch_to.window(x_window)
    sleep(7)
    comment_input = drivers.find_element(By.XPATH , value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div')
    comment_input.send_keys(comment.response())
    sleep(2)
    post_btn = drivers.find_element(By.XPATH , value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
    post_btn.click()
    sleep(8)
    try:
        sleep(2)
        got_it = drivers.find_element(By.XPATH , value='//*[@id="layers"]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/button')
        got_it.click()
    except NoSuchElementException:
        pass
    sleep(60)
















