import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException

insta_id = "your accountusername"
famous_id = "famous_id_username"
insta_pass = "your account password"
chrome_driver_path = "C:\Chrome driver\chromedriver.exe"

class InstaFollower:

    def __init__(self, path):
        self.service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.service)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)

        id_field = self.driver.find_element(By.NAME, 'username')
        id_field.send_keys(insta_id)

        password_field = self.driver.find_element(By.NAME, 'password')
        password_field.send_keys(insta_pass)

        login_key = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_key.click()

        time.sleep(5)

    def pop_up(self):
        save_info_key = self.driver.find_element(By.XPATH,
                                            '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')
        save_info_key.click()

        time.sleep(3)

        notification_key = self.driver.find_element(By.XPATH,
                                               '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        notification_key.click()

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{famous_id}")

        time.sleep(4)

        find_follow = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div')
        find_follow.click()
        time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CLASS_NAME,'x1qjc9v5.x9f619.x78zum5.xdt5ytf.x1iyjqo2.xl56j7k')
        time.sleep(2)
        print(len(all_buttons))
        for button in all_buttons:
            time.sleep(3)
            button.click()
            time.sleep(2)
            # except ElementClickInterceptedException:
            #     time.sleep(2)
            #     cancel_button = self.driver.find_element(By.CLASS_NAME,'_a9--._a9_1')
            #     cancel_button.click()
            #


bot = InstaFollower(chrome_driver_path)
bot.login()
bot.pop_up()
bot.find_followers()
bot.follow()
time.sleep(10000)
