import pytest
from tests.saucedemo_page.login_page import LoginPage
from selenium.webdriver.common.by import By

@pytest.mark.order_test

def test_order_add_cart(chrome_browser):
    url = "https://www.saucedemo.com/"
    login_page = LoginPage(chrome_browser)
    login_page.open_page(url)
    login_page.login_standard(chrome_browser)

    login = chrome_browser.find_element(By.ID, "login-button")
    login.click()

    backpack_add = chrome_browser.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
    backpack_add.click()

    backpack_remove = chrome_browser.find_elements(By.CSS_SELECTOR, '[data-test="remove-sauce-labs-backpack')

    #Verify the button change to Remove
    assert backpack_remove[0].text == "Remove"
    #There should an asset for Badge number

def test_order_remove(chrome_browser):
    url = "https://www.saucedemo.com/"
    login_page = LoginPage(chrome_browser)
    login_page.open_page(url)
    login_page.login_standard(chrome_browser)

    login = chrome_browser.find_element(By.ID, "login-button")
    login.click()

    backpack_add = chrome_browser.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
    backpack_add.click()

    chrome_browser.implicitly_wait(2)

    backpack_remove = chrome_browser.find_element(By.CSS_SELECTOR, '[data-test="remove-sauce-labs-backpack"]')
    backpack_remove.click()

    chrome_browser.implicitly_wait(2)
    backpack_add_displayed = chrome_browser.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')


    assert backpack_add_displayed.text == "Add to cart"




