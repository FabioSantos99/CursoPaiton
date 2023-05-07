from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = Options()
options.add_argument("start-maximized")
options.add_argument('disable-notifications')

options.add_argument('profile-directory=Default')
options.add_argument('user-data-dir=/tmp/browser')

webdriver_service = Service('C:\webdrivers\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=webdriver_service)
wait = WebDriverWait(driver, 15)

url = "https://forum.gatapop.com/"

driver.get(url)

wait.until(EC.element_to_be_clickable((By.NAME, 'q'))).send_keys("Eilin Castaño")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#elSearch > form > button > i'))).click()

wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ipsMatch1'))).click()
sleep(3)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                       '#ipsLayout_mainArea > div.cTopic.ipsClear.ipsSpacer_top > div.cTopicPostArea.ipsBox.ipsBox_transparent.ipsAreaBackground.ipsPad.ipsSpacer_top > form > div > div.ipsComposeArea_editor > div > div.ipsContained > div.ipsComposeArea_dummy.ipsJS_show'))).click()
sleep(3)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#cke_1_contents > div > p'))).send_keys("Será que o OF dela é bom")
sleep(2)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#ipsLayout_mainArea > div.cTopic.ipsClear.ipsSpacer_top > div.cTopicPostArea.ipsBox.ipsBox_transparent.ipsAreaBackground.ipsPad.ipsSpacer_top > form > div > div.ipsComposeArea_editor > ul > li:nth-child(2) > button'))).click()


