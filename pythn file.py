import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#service clause used t avaid the "executable path is deprecated" errr
from selenium.webdriver.chrome.service import Service

class Amazon:
    def __init__(self):
        service = Service(executable_path=ChromeDriverManager().install())
        opt = webdriver.ChromeOptions()
        opt.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=service, options=opt)

    def browser_open(self):
        self.driver.get('https://www.amazon.in/')
        print(self.driver.get_cookie('session-id'))


        self.driver.get('https://www.browserstack.com/guide/wait-commands-in-selenium-webdriver')
        self.driver.get('https://www.edureka.co/community/34464/how-can-i-travel-forward-and-back'
                        '-in-a-browser-using-selenium')
        self.driver.fullscreen_window()
        time.sleep(2)
        self.driver.back()
        self.driver.back()
        time.sleep(2)
        self.driver.forward()
        print(self.driver.current_url)
        print(self.driver.application_cache)

    def new_tab(self):
        self.driver.get('https://www.amazon.in/')

# Through selenium function open the new tab
        self.driver.switch_to.new_window()
        self.driver.get('https://www.browserstack.com/')
        self.driver.switch_to.window(self.driver.window_handles[0])

# Through Java Script open the new tab
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[2])


o = Amazon()
o.browser_open()
o.new_tab()