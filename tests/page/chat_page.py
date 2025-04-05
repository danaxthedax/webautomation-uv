from warnings import catch_warnings
from pytest_selenium import driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class ChatPage:
    def verify_text_element(self, text_element):

        try:
          specific_element =  self.driver().find_element(By.XPATH, f"//*[contains(text(), '{text_element}')]")
          specific_element_text = specific_element.text
        except NoSuchElementException:
            specific_element = ""


