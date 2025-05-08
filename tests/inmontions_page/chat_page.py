from warnings import catch_warnings
from pytest_selenium import driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class ChatPage:
    def __init__(self,driver):
        self.driver = driver

    def find_name_input(self, driver):
        self.driver.find_element(By.ID, "customer-name")

    def find_email_input(self,driver):
        self.driver.chrome_browser.find_element(By.ID, "customer-email")

    def find_chat_submit(self,driver):
        self.driver.chrome_browser.find_element(By.ID, "sales-chat-submit")