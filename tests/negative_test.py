import values
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize(
    "username_input, password_input",
    [
        ("az", "Password123"),
        ("zcasdqwezxcasdqwezxca", "Password123")
    ]
)


def test_username_length(driver, username_input, password_input,):
    # testing multiple successful logins
    wait = WebDriverWait(driver, 2)
    driver.get(values.site)

    # Input the parameterized username
    username = wait.until(EC.visibility_of_element_located((By.ID, values.username_field)))
    username.send_keys(username_input)

    # Input the parameterized password
    password = driver.find_element(By.ID, values.password_field)
    password.send_keys(password_input)

    login_button = driver.find_element(By.ID, values.signin_button)
    login_button.click()

    success_message = wait.until(EC.visibility_of_element_located((By.ID, values.logon_message)))

    assert "Username must be between 3 and 20 characters" in success_message.text


@pytest.mark.parametrize(
    "username_input_length, password_input_length",
    [
        ("admin", "1234567"),
        ("admin", "1234567890123456789012345678901")
    ]
)


def test_password_length(driver, username_input_length, password_input_length):
    # testing multiple successful logins
    wait = WebDriverWait(driver, 2)
    driver.get(values.site)

    # Input the parameterized username
    username = wait.until(EC.visibility_of_element_located((By.ID, values.username_field)))
    username.send_keys(username_input_length)

    # Input the parameterized password
    password = driver.find_element(By.ID, values.password_field)
    password.send_keys(password_input_length)

    login_button = driver.find_element(By.ID, values.signin_button)
    login_button.click()

    success_message = wait.until(EC.visibility_of_element_located((By.ID, values.logon_message)))

    assert "Password must be between 8 and 30 characters" in success_message.text


@pytest.mark.parametrize(
    "username_input_mismatch, password_input_mismatch",
    [
        ("admin", "UserPass123")
    ]
)


def test_username_password_mismatch(driver, username_input_mismatch, password_input_mismatch):
    # testing multiple successful logins
    wait = WebDriverWait(driver, 2)
    driver.get(values.site)

    # Input the parameterized username
    username = wait.until(EC.visibility_of_element_located((By.ID, values.username_field)))
    username.send_keys(username_input_mismatch)

    # Input the parameterized password
    password = driver.find_element(By.ID, values.password_field)
    password.send_keys(password_input_mismatch)

    login_button = driver.find_element(By.ID, values.signin_button)
    login_button.click()

    success_message = wait.until(EC.visibility_of_element_located((By.ID, values.logon_message)))

    assert "Invalid username or password" in success_message.text
