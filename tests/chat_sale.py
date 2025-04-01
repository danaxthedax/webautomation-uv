import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tests.page.start_page import StartPage

@pytest.mark.chat_sale
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

def test_invalid_email(chrome_browser):
    url = "http://automationpractice.com/"
    start_page = StartPage(chrome_browser)
    start_page.open_page(url)
    start_page.select_image(chrome_browser)


    chat_with_sale = chrome_browser.find_elements("xpath",
                                                  "//*[contains(@class, 'ppb-button') and"
                                                  " contains(@class, 'btn-primary-chat') and "
                                                  "contains(@class, 'chat-btn-popup')]")
    ActionChains(chrome_browser) \
        .scroll_to_element(chat_with_sale[0]) \
        .scroll_by_amount(0, 500) \
        .perform()
    chat_with_sale[0].click()
    chrome_browser.implicitly_wait(2)
    chrome_browser.switch_to.window(chrome_browser.window_handles[1])
    chrome_browser.implicitly_wait(2)
    email_input = chrome_browser.find_element(By.ID, "customer-email")
    chrome_browser.implicitly_wait(2)
    email_input.click()
    ActionChains(chrome_browser)\
        .key_down(Keys.SHIFT)\
        .send_keys("notvaild")\
        .perform()
    start_chat = chrome_browser.find_element(By.ID, "sales-chat-submit")
    start_chat.click()
    email_error = chrome_browser.find_elements("xpath",
                                                  "//*[contains(@class, 'char-input-wrapper') and"
                                                  "contains(@class, 'char-login-error')]")
    print("This is the result: " + email_error)

    assert "This doesn't look like an email address." in email_error
