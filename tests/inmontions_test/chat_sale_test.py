import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


from tests.inmontions_page.start_page import StartPage
from tests.inmontions_page.home_page import HomePage

@pytest.mark.chat_sale_test
def test_three_sales_chats(chrome_browser):
    #verify all three chat option for Chat with sales are working
    url = "http://automationpractice.com/"
    start_page = StartPage(chrome_browser)
    start_page.open_page(url)
    start_page.select_image(chrome_browser)


    original_window = chrome_browser.current_window_handle
    total_chat_with_sales = 0

    chat_with_sale = chrome_browser.find_elements("xpath",
                                          "//*[contains(@class, 'ppb-button') and"
                                          " contains(@class, 'btn-primary-chat') and "
                                          "contains(@class, 'chat-btn-popup')]")

    for cla in chat_with_sale:
        ActionChains(chrome_browser) \
            .scroll_to_element(cla) \
            .scroll_by_amount(0, 500) \
            .perform()
        cla.click()
        chrome_browser.switch_to.window(chrome_browser.window_handles[1])
        verify_chat = chrome_browser.find_element("xpath", "//*[contains(text(), 'Chat with Sales')]")
        if verify_chat != "":
            print("Passed")
            total_chat_with_sales+=1
        chrome_browser.close()
        chrome_browser.switch_to.window(original_window)

    assert total_chat_with_sales == 3

def test_invalid_email_error(chrome_browser):
    url = "http://automationpractice.com/"
    start_page = StartPage(chrome_browser)
    start_page.open_page(url)
    start_page.select_image(chrome_browser)

    home_page = HomePage(chrome_browser)
    home_page.select_chat_with_sales(chrome_browser)
    chrome_browser.implicitly_wait(10)

    chrome_browser.switch_to.window(chrome_browser.window_handles[1])
    chrome_browser.implicitly_wait(10)

    your_name = chrome_browser.find_element(By.ID, "customer-name")
    your_name.click()
    your_name.send_keys("Test Testsson")

    email_input = chrome_browser.find_element(By.ID, "customer-email")
    email_input.click()
    email_input.send_keys("not vaild")
    chrome_browser.implicitly_wait(10)

    start_chat = chrome_browser.find_element(By.ID, "sales-chat-submit")
    start_chat.click()

    email_error = chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'look like an email address.')]")

    assert email_error.text == "This doesn't look like an email address."

def test_name_required_error(chrome_browser):
    url = "http://automationpractice.com/"
    start_page = StartPage(chrome_browser)
    start_page.open_page(url)
    start_page.select_image(chrome_browser)

    home_page = HomePage(chrome_browser)
    home_page.select_chat_with_sales(chrome_browser)
    chrome_browser.implicitly_wait(10)

    chrome_browser.switch_to.window(chrome_browser.window_handles[1])
    chrome_browser.implicitly_wait(10)

    email_input = chrome_browser.find_element(By.ID, "customer-email")
    chrome_browser.implicitly_wait(10)
    email_input.click()
    email_input = chrome_browser.find_element(By.ID, "customer-email")
    email_input.click()
    email_input.send_keys("test@gmail.com")
    start_chat = chrome_browser.find_element(By.ID, "sales-chat-submit")
    start_chat.click()
    chrome_browser.implicitly_wait(10)
    name_error = chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Name is required.')]")

    assert name_error.text == "Name is required."

def test_valid_name_email(chrome_browser):
    url = "http://automationpractice.com/"
    start_page = StartPage(chrome_browser)
    start_page.open_page(url)
    start_page.select_image(chrome_browser)

    home_page = HomePage(chrome_browser)
    home_page.select_chat_with_sales(chrome_browser)

    chrome_browser.switch_to.window(chrome_browser.window_handles[1])
    chrome_browser.implicitly_wait(10)


    your_name = chrome_browser.find_element(By.ID, "customer-name")
    your_name.click()
    your_name.send_keys("Test Testsson")

    email_input = chrome_browser.find_element(By.ID, "customer-email")
    email_input.click()
    email_input.send_keys("test@gmail.com")


    chrome_browser.implicitly_wait(10)
    chat_submit = chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Start Chat')]")
    chat_submit.click()

    chrome_browser.implicitly_wait(10)
    chat_with_us = chrome_browser.find_element(By.ID, "webWidget")
    assert chat_with_us == "Chat with us"