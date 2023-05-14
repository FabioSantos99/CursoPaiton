from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("http://www.google.com/")

# Abre uma nova aba
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + 't')

# Carrega a nova aba
driver.get('http://stackoverflow.com/')

# Fecha a aba
