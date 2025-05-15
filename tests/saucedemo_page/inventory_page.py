from pytest_selenium import driver
from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self,driver):
        self.driver = driver

    def select_cart(self,driver):
        cart_link = self.driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
        cart_link.click()