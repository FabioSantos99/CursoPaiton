from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()

browser.get("https://www.google.com")

elem = browser.find_element(By.CLASS_NAME,'gLFyf')
elem.send_keys('PythonBr')
elem.send_keys(Keys.RETURN)


input()

