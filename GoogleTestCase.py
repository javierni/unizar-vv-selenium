import unittest
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('https://www.zaragoza.es')
        self.assertIn('La Web de la Ciudad de Zaragoza', self.browser.title)
        response = input('Esperando para ver la página web. Pulsa cualquier tecla para salir: ')

if __name__ == '__main__':
    unittest.main(verbosity=2)