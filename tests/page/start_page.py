#Start page of http://automationpractice.com/
from pytest_selenium import driver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class StartPage:
    def __init__(self,driver):
        self.driver = driver

    def open_page(self,url):
        self.driver.get(url)

    def select_image(self, driver):
        image_select = self.driver.find_elements("xpath", "//img[@src]")
        image_select[0].click()
        driver.implicitly_wait(2)

    def verify_successful_select(self):
        try:
            login_button = self.driver.find_element(By.LINK_TEXT,"Login")
            return login_button.is_displayed()
        except NoSuchElementException:
            assert False, "Login button are missing"
