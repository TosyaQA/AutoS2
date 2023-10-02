import yaml
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

with open('./config.yaml') as f:
    config = yaml.safe_load(f)

service = Service(config['driver_path'])
options = webdriver.ChromeOptions()

class Site:
    def __init__(self, address):
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        self.driver.get(address)
        time.sleep(config['sleep_time'])

    def find_element(self, mode, path):
        if mode == 'css':
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == 'xpath':
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def find_elements(self, mode, path):
        if mode == 'css':
            elements = self.driver.find_elements(By.CSS_SELECTOR, path)
        elif mode == 'xpath':
            elements = self.driver.find_elements(By.XPATH, path)
        else:
            elements = None
        return elements
    
    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)
    
    def close(self):
        self.driver.close()