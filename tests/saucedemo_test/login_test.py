import pytest
from tests.saucedemo_page.login_page import LoginPage
from selenium.webdriver.common.by import By
#swaplogin to test login

@pytest.mark.login_test
def test_login_standard(chrome_browser):
    url = "https://www.saucedemo.com/"
    login_page = LoginPage(chrome_browser)
    login_page.open_page(url)

    login_page.login_standard(chrome_browser)

    login = chrome_browser.find_element(By.ID, "login-button")
    login.click()

    menu = chrome_browser.find_element(By.ID, "react-burger-menu-btn")

    assert menu != ""

def test_login_standard_failed(chrome_browser):
    #This test-case is to display if there were error to login
    url = "https://www.saucedemo.com/"
    login_page = LoginPage(chrome_browser)
    login_page.open_page(url)

    username = chrome_browser.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = chrome_browser.find_element(By.ID, "password")
    password.send_keys("secret_ce")

    login = chrome_browser.find_element(By.ID, "login-button")
    login.click()

    menu = chrome_browser.find_element(By.ID, "react-burger-menu-btn")

    assert menu != ""

def test_login_locked_user(chrome_browser):
    url = "https://www.saucedemo.com/"
    login_page = LoginPage(chrome_browser)
    login_page.open_page(url)

    username = chrome_browser.find_element(By.ID, "user-name")
    username.send_keys("locked_out_user")

    password = chrome_browser.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login = chrome_browser.find_element(By.ID, "login-button")
    login.click()

    error_message = chrome_browser.find_element(By.XPATH,  "//*[contains(text(), 'Epic sadface: Sorry, this user has been locked out.')]")

    assert error_message.text == "Epic sadface: Sorry, this user has been locked out."