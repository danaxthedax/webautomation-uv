import pytest
from tests.page.start_page import StartPage

@pytest.mark.select
def test_select_inmotion(chrome_browser):
    #Select inmotion hosting to get to home page
    url = "http://automationpractice.com/"
    start_page = StartPage(chrome_browser)

    #Open page
    start_page.open_page(url)

    start_page.select_image(chrome_browser)