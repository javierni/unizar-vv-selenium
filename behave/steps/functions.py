from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://www.zaragoza.es"

class MyFunctions():
    
    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.driver = webdriver.Firefox()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.driver.quit()
    
    def enterMainPage(self):
        self.driver = webdriver.Firefox()
        self.driver.get(link)

    def clickSearchButton(self):
        searchButton = self.driver.find_element(By.LINK_TEXT, 'Buscador')
        searchButton.click()

    def enterKeyword(self, keyword):
        elem = self.driver.find_element(By.NAME, 'query')  # Find the search box
        elem.send_keys(keyword + Keys.RETURN)

    def resultsPageIsOpen(self):
        element = WebDriverWait(self.driver, 10).until(EC.title_contains("Buscador. Ayuntamiento de Zaragoza"))
        # assert 'Número de resultados' in self.driver.page_source
