from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def make_driver():
    chrome_options = Options()
    # cloud arrangements
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    return driver

def main():
    driver = make_driver()
    city_list = [
        "Nyíregyháza", "Kecskemét", "Székesfehérvár", "Szombathely",
        "Szolnok", "Tatabánya", "Sopron", "Kaposvár",
        "Veszprém", "Békéscsaba", "Zalaegerszeg", "Eger", "Nagykanizsa"
    ]

    gym_list = []
    for city in city_list:
        print(f"Searching for {city}")
        driver.get(f"https://www.google.com/maps/place/{city}")
        sleep(3)
        search_box = driver.find_element(By.XPATH ,value='//*[@name="q"]')
        search_box.clear()
        search_box.send_keys(f"GYM in {city} Hungary")
        search_box.send_keys(Keys.ENTER)
        sleep(5)
        try:
            scrollable_div = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="feed"]'))
            )
        except:
            print("Sonuç paneli bulunamadı.")
            return
        last_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
        while True:
            driver.execute_script('arguments[0].scrollBy(0, arguments[0].scrollHeight)', scrollable_div)
            sleep(10)
            new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
            if new_height == last_height:
                break
            last_height = new_height
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        gym_numbers = driver.find_elements(By.XPATH, value='//*[@class="NrDZNb"]/div/div')
        for gym in gym_numbers:
            gym_dict = {}
            gym_dict["gym_name"] = gym.text
            gym_get_info = soup.find("a", {"aria-label": f"{gym.text}"})["href"]
            driver.get(gym_get_info)
            sleep(3)
            try:
                gym_address =  driver.find_element(By.XPATH ,value='//*[@class="rogA2c "]/div').text
                gym_dict["gym_address"] = gym_address
            except Exception as e:
                gym_dict["gym_address"] = "None"
            try:
                gym_website = driver.find_element(By.XPATH ,value='//*[@class="rogA2c ITvuef"]/div').text
                gym_dict["gym_website"] = "https://www." + gym_website
            except NoSuchElementException:
                gym_dict["gym_website"] = "None"
            try:
                html2 = driver.page_source
                soup2 = BeautifulSoup(html2, 'html.parser')
                gym_tel_q = soup2.find("span", {"class": "google-symbols NhBTye PHazN"})
                gym_tel = soup2.find_all("button", {"class": "CsEnBe"})[-2]["aria-label"][9:-1]
                if gym_tel_q:
                    gym_dict["gym_tel"] = gym_tel
                else:
                    gym_dict["gym_tel"] = "None"
            except Exception as e:
                gym_dict["gym_tel"] = "None"
            gym_list.append(gym_dict)
            print("finished gym searching for city")
    gym_df = pd.DataFrame(gym_list)
    gym_df.to_excel("gym_in_Nyíregyháza_end.xlsx", index=False)

if __name__ == "__main__":
    main()