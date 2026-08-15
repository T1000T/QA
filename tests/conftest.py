import pytest
from selenium import webdriver
from automation.pages.login_page import LoginPage


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    # Initialize a completely fresh browser instance for the test
    chrome_driver = webdriver.Chrome(options=options)

    yield chrome_driver

    chrome_driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)