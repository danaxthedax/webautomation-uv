import pytest
from tests.page.start_page import StartPage

@pytest.mark.homepage
def test_select_inmotion(chrome_browser):
    #Select inmotion hosting to get to home page
    url = "http://automationpractice.com/"
    start_page = StartPage(chrome_browser)

    #Open page
    start_page.open_page(url)
    start_page.select_image(chrome_browser)
    assert chrome_browser.title == "InMotion Hosting | Premier Web Host & Server Provider"

def test_select_inmotion_failes(chrome_browser):
    #Select inmotion hosting to get to home page, failed test
    url = "http://automationpractice.com/"
    start_page = StartPage(chrome_browser)

    #Open page
    start_page.open_page(url)
    start_page.select_image(chrome_browser)
    assert chrome_browser.title == "Not Correct"