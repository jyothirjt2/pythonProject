
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
    def home_page(self):
        self.driver.get("https://www.amazon.in/")
        a = ActionChains(self.driver)
        mouse_hover=self.driver.find_element(By.ID,"icp-nav-flyout")
        a.move_to_element(mouse_hover).perform()

a=Amazon()
a.home_page()