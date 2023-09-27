from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import dotenv_values
import logging
import time

class Scraping:
    def __init__(self):
        self.env = dotenv_values('.env')
        options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(options=options)

    def run(self):
        # Define as configurações do log
        logging.basicConfig(format='%(asctime)s :: %(levelname)s :: %(message)s', filename='app.log', filemode='w', level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S')
        
        logging.info('Navigate to page')

        # Navaga para a página de principal do Airbnb
        self.browser.get(self.env.get('URL'))

        time.sleep(2)

        # Fecha o browser
        self._fecha_browser()
        logging.info('Closed the browser')
    
    # Método para fechar o browser
    def _fecha_browser(self):
        time.sleep(5)
        # Fecha o browser
        self.browser.close()
