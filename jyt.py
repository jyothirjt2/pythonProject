
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
class Amazon:
    def __init__(self):
        service = Service(executable_path=ChromeDriverManager().install())
        opt = webdriver.ChromeOptions()
        opt.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=service, options=opt)
    def Cookie_handle(self):
        self.driver.get("https://www.amazon.in/")
        cookies=self.driver.get_cookies()
        print(cookies)
        print(len(cookies))

        cookie={'name':'mycookie','value':'12790jynd'}
        self.driver.add_cookie(cookie)
        print(cookies)
        print(len(cookies))

        self.driver.delete_cookie(cookie)
        print(len(cookies))
    def ScreenShot(self):
        self.driver.get("https://www.amazon.in/")
        # self.driver.get_screenshot_as_file("C:\\Users\\jyoth\\Documents\\srnsht.png")
        self.driver.get_screenshot_as_png().s



a=Amazon()
# a.Cookie_handle()
a.ScreenShot()