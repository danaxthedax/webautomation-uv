#Home page selection
from pytest_selenium import driver
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    def select_chat_with_sales(self,driver):
        chat_with_sale = self.driver.find_elements("xpath",
                                                      "//*[contains(@class, 'ppb-button') and"
                                                      " contains(@class, 'btn-primary-chat') and "
                                                      "contains(@class, 'chat-btn-popup')]")
        ActionChains(self.driver) \
            .scroll_to_element(chat_with_sale[0]) \
            .scroll_by_amount(0, 500) \
            .perform()
        chat_with_sale[0].click()
