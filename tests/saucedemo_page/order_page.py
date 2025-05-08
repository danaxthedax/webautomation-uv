from pytest_selenium import driver
from selenium.webdriver.common.by import By

class OrderPage:
    def __init__(self,driver):
        self.driver = driver

    def open_page(self,url):
        self.driver.get(url)
