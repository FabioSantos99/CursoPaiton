from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = Options()
options.add_argument("start-maximized")

webdriver_service = Service('C:\webdrivers\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=webdriver_service)
wait = WebDriverWait(driver, 10)

url = "https://www.instagram.com"

driver.get(url)
wait.until(EC.element_to_be_clickable((By.NAME, "username"))).send_keys('joaodonad')
wait.until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys('Camis@100')
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]'))).click()
sleep(3)

wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'_ac8f'))).click()
sleep(2)

wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'_a9-- _a9_1'))).click()