import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pytest_metadata.plugin import metadata_key

@pytest.fixture()
def chrome_browser():
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

def pytest_html_report_title(report):
        report.title = "Automation Report for Daniel Axelsson"

def pytest_configure(config):
        config.stash[metadata_key]["Project"] = "Webautomation-UV"

