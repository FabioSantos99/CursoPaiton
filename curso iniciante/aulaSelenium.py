from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
navegador.get('https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_videoselenium')
navegador.find_element(By.XPATH, '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys("Fabio")
navegador.find_element(By.XPATH, '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys("louiscccccdacosta@gmail.com")
navegador.find_element(By.XPATH, '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[3]/div/input').send_keys("(11) 984443-5784")
navegador.find_element(By.XPATH, '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/button/span/b').click()

time.sleep(6)
