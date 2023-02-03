from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class automation:
    def __init__(self):
        service = Service(executable_path=ChromeDriverManager().install())
        opt = webdriver.ChromeOptions()
        opt.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=service, options=opt)
    def window_handles(self):
        self.driver.get("https://demo.automationtesting.in/Windows.html")
        self.driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click()
        print(self.driver.current_window_handle)
        handles=self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            print(self.driver.title)
            if self.driver.title == "frames & windows":
                self.driver.close()

























a=automation()
a.window_handles()

