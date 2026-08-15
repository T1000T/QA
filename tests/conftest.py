import pytest
import pytest_html
from pytest_html import extras
import os
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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = os.path.join(
                "screenshots",
                f"{item.name}.png"
            )

            driver.save_screenshot(screenshot_path)

            # Attach screenshot to pytest-html
            if hasattr(report, "extras"):
                report.extras.append(
                    pytest_html.extras.image(screenshot_path)
                )
