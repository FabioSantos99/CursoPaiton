from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

elemento = ("id", "meu_elemento")
driver.find_element(*elemento)  # O asterisco (*) desempacota a tupla como argumentos separados

driver.quit()


from selenium import webdriver

driver = webdriver.Chrome()

seletores = ["id", "name", "class"]
for seletor in seletores:
    elemento = driver.find_element_by_css_selector(f"[{seletor}='meu_elemento']")
    # Faça algo com o elemento

driver.quit()


from selenium import webdriver

driver = webdriver.Chrome()

elemento = {
    "seletor": "id",
    "valor": "meu_elemento"
}
elemento_encontrado = driver.find_element(elemento["seletor"], elemento["valor"])
# Faça algo com o elemento

driver.quit()


# Usar listas,tuplas, dicionarios items

from selenium import webdriver

driver = webdriver.Chrome()

elementos = [("id", "elemento1"), ("name", "elemento2"), ("class", "elemento3")]

for seletor, valor in elementos:
    elemento = driver.find_element(seletor, valor)
    # Faça algo com o elemento

driver.quit()


from selenium import webdriver

driver = webdriver.Chrome()

elementos = ["elemento1", "elemento2", "elemento3"]

for valor in elementos:
    elemento = driver.find_element_by_id(valor)
    # Faça algo com o elemento

driver.quit()


from selenium import webdriver

driver = webdriver.Chrome()

elementos = {
    "elemento1": "id",
    "elemento2": "name",
    "elemento3": "class"
}

for valor, seletor in elementos.items():
    elemento = driver.find_element(seletor, valor)
    # Faça algo com o elemento

driver.quit()



