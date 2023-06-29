from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

urls = ['https://www.youtube.com', 'https://www.google.com', 'https://www.facebook.com']
sleeps = (7, 6, 5)
for url in urls:
    for wake in sleeps:
     driver.get(url)
     sleep(wake)

