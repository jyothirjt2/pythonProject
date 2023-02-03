from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path=ChromeDriverManager().install())
opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, options=opt)
driver.get("https://www.amazon.in/")


# cookies=driver.get_cookies()
# print(cookies)
# print(len(cookies))
#
# cookie={'name':'mycookie','value':'12790jynd'}
# driver.add_cookie(cookie)
# print(cookies)
# print(len(cookies))

# driver.delete_cookie(cookie1)
# print(len(cookies))





