from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = Options()
options.add_argument("start-maximized")

webdriver_service = Service('C:\webdrivers\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=webdriver_service)
wait = WebDriverWait(driver, 10)

url = "https://wolf.bet/login"

driver.get(url)
sleep(2)
wait.until(EC.element_to_be_clickable((By.NAME, "login"))).send_keys('MrSatoshi')
wait.until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys('Gbcjp2004')
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div[1]/div[1]/div/div[2]/div[2]/form/button'))).click()
sleep(5)
wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div[1]/header/div/div[2]/div[2]/button/svg/path[1]'))).click()
wait.until(EC.element_to_be_clickable((By.ID,'chat-input'))).send_keys('Hi everyone')
wait.until(EC.element_to_be_clickable((By.NAME,'chat-message-submit'))).click()