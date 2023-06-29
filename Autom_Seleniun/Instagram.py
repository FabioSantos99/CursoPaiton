from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = Options()
options.add_argument("start-maximized")
options.add_argument("--mute-audio--")


webdriver_service = Service('C:\webdrivers\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=webdriver_service)
wait = WebDriverWait(driver, 10)

url = "https://www.instagram.com"

driver.get(url)
sleep(2)
wait.until(EC.element_to_be_clickable((By.NAME, "username"))).send_keys('joaodonad')
wait.until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys('Camis@100')
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button > div"))).click()

