from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://zaragoza.es')
assert 'Zaragoza' in browser.title
# Desplegar la caja de búsqueda
searchButton = browser.find_element(By.LINK_TEXT, 'Buscador')
searchButton.click()
# Localizar la caja de búsqueda
elem = browser.find_element(By.NAME, 'query')
elem.send_keys('turismo' + Keys.RETURN)
response = input('Esperando para ver la página web, pulsa cualquier teclar: ')
browser.quit()