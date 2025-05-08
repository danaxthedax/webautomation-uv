from pytest_selenium import driver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def open_page(self,url):
        self.driver.get(url)

    def login_standard(self, driver):
        username = self.driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")

        password = self.driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        login = self.driver.find_element(By.ID, "login-button")
        login.click()