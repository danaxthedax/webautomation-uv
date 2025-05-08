#Start inmontions_page of http://automationpractice.com/
from pytest_selenium import driver


class StartPage:
    def __init__(self,driver):
        self.driver = driver

    def open_page(self,url):
        self.driver.get(url)

    def select_image(self, driver):
        image_select = self.driver.find_elements("xpath", "//img[@src]")
        image_select[0].click()
        driver.implicitly_wait(2)
