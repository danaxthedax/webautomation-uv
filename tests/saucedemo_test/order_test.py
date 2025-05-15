import pytest
from tests.saucedemo_page.login_page import LoginPage
from tests.saucedemo_page.inventory_page import InventoryPage
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

def test_correct_order_in_cart_flex(chrome_browser):
    #same testcase above but not hardcode. Compare the first item in inventroy and in cart
    url = "https://www.saucedemo.com/"
    login_page = LoginPage(chrome_browser)
    login_page.open_page(url)
    login_page.login_standard(chrome_browser)

    inventory_lists = chrome_browser.find_elements(By.CSS_SELECTOR, '[data-test="inventory-list"]')
    first_inventory_list = inventory_lists[0]
    first_inventory_item = first_inventory_list.find_element(By.CSS_SELECTOR, '[data-test="inventory-item"]')
    first_inventory_item_desc = first_inventory_item.find_element(By.CSS_SELECTOR,'[data-test="inventory-item-desc"]' )

    print(first_inventory_item_desc.text)

    add_to_cart_button = first_inventory_item.find_element(By.TAG_NAME, 'button')
    add_to_cart_button.click()

    cart_link = chrome_browser.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    chrome_browser.implicitly_wait(5)
    cart_link.click()

    item_in_cart = chrome_browser.find_elements(By.CSS_SELECTOR, '[data-test="inventory-item"]')
    first_item_in_cart = item_in_cart[0]
    item_in_cart_text = first_item_in_cart.find_element(By.CSS_SELECTOR, '[data-test="inventory-item-desc"]')


    assert first_inventory_item_desc.text == item_in_cart_text.text

