import pytest
from selenium.webdriver import ActionChains
from tests.page.start_page import StartPage

@pytest.mark.select
def verify_three_sales_chats(chrome_browser):
    #verify all three chat option for Chat with sales are working
    url = "http://automationpractice.com/"
    start_page = StartPage(chrome_browser)
    start_page.open_page(url)
    start_page.select_image(chrome_browser)
    chrome_browser.implicitly_wait(2)

    original_window = chrome_browser.current_window_handle
    total_chat_with_sales = 0

    chat_with_sale = chrome_browser.find_elements("xpath",
                                          "//*[contains(@class, 'ppb-button') and"
                                          " contains(@class, 'btn-primary-chat') and "
                                          "contains(@class, 'chat-btn-popup')]")

    for cla in chat_with_sale:
        ActionChains(chrome_browser) \
            .scroll_to_element(cla) \
            .scroll_by_amount(0, 200) \
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

