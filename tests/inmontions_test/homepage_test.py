import pytest
from tests.inmontions_page.start_page import StartPage

@pytest.mark.homepage_test
def test_select_inmotion(chrome_browser):
    #Select inmotion hosting to get to home inmontions_page
    url = "http://automationpractice.com/"
    start_page = StartPage(chrome_browser)

    #Open inmontions_page
    start_page.open_page(url)
    start_page.select_image(chrome_browser)
    assert chrome_browser.title == "Best Web Hosting, VPS, Dedicated Servers & Domains | InMotion Hosting"

def test_select_inmotion_failes(chrome_browser):
    #Select inmotion hosting to get to home inmontions_page, failed test
    url = "http://automationpractice.com/"
    start_page = StartPage(chrome_browser)

    #Open inmontions_page
    start_page.open_page(url)
    start_page.select_image(chrome_browser)
    assert chrome_browser.title == "Not Correct"