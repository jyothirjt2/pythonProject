from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
services = Service(executable_path=ChromeDriverManager().install())
opt = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=services,options=opt)

driver.get("https://demo.automationtesting.in/Windows.html")
driver.find_element(By.XPATH,"//*[@id='Tabbed']/a/button").click()
