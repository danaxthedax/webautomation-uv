import pytest
from tests.saucedemo_page.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

@pytest.mark.order_test

def test_order_add_cart(chrome_browser):
    url = "https://www.saucedemo.com/"
    login_page = LoginPage(chrome_browser)
    login_page.open_page(url)
    login_page.login_standard(chrome_browser)

    backpack_add = chrome_browser.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
    backpack_add.click()

    backpack_remove = chrome_browser.find_elements(By.CSS_SELECTOR, '[data-test="remove-sauce-labs-backpack')
    badge = chrome_browser.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')

    #Verify the button change to Remove
    assert backpack_remove[0].text == "Remove"
    assert badge.text == "1"

def test_order_remove(chrome_browser):
    url = "https://www.saucedemo.com/"
    login_page = LoginPage(chrome_browser)
    login_page.open_page(url)
    login_page.login_standard(chrome_browser)

    backpack_add = chrome_browser.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
    backpack_add.click()
    chrome_browser.implicitly_wait(5)

    backpack_remove = chrome_browser.find_elements(By.CSS_SELECTOR, '[data-test="remove-sauce-labs-backpack')

    print(backpack_remove)
    backpack_remove[0].click()

    backpack_add_displayed = chrome_browser.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')

    assert backpack_add_displayed.text == "Add to cart"
    #Assert that badge are not displayed

def test_correct_order_in_cart(chrome_browser):
    url = "https://www.saucedemo.com/"
    login_page = LoginPage(chrome_browser)
    login_page.open_page(url)
    login_page.login_standard(chrome_browser)

    backpack_add = chrome_browser.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
    backpack_add.click()

    cart_link = chrome_browser.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    chrome_browser.implicitly_wait(5)
    cart_link.click()

    bag_name = chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'Sauce Labs Backpack')]")
    bag_desc = chrome_browser.find_element(By.XPATH, "//*[contains(text(), 'carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.')]")

    assert bag_desc.text == "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection."
    assert bag_name.text == "Sauce Labs Backpack"



