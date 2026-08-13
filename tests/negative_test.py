import values
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize(
    "username_input_boundary, password_input_boundary",
    [
        ("az", "Password123"),
        ("zcasdqwezxcasdqwezxca", "Password123"),
        ("admin", "Passwor"),
        ("admin", "Password123Password123Password1")

    ]
)


def test_username_password_out_of_boundaries(driver, username_input_boundary, password_input_boundary):
    # testing out of boundaries
    wait = WebDriverWait(driver, 2)
    driver.get(values.site)

    # Input the parameterized username
    username = wait.until(EC.visibility_of_element_located((By.ID, values.username_field)))
    username.send_keys(username_input_boundary)

    # Input the parameterized password
    password = driver.find_element(By.ID, values.password_field)
    password.send_keys(password_input_boundary)

    login_button = driver.find_element(By.ID, values.signin_button)
    login_button.click()

    error_message = wait.until(EC.visibility_of_element_located((By.ID, values.logon_message)))

    assert "Username must be between 3 and 20 characters" in error_message.text or "Password must be between 8 and 30 characters" in error_message.text


@pytest.mark.parametrize(
    "username_input_length, password_input_length",
    [
        ("admin", "1234567"),
        ("admin", "1234567890123456789012345678901")
    ]
)


def test_password_length(driver, username_input_length, password_input_length):
    # testing short/long password
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

    error_message = wait.until(EC.visibility_of_element_located((By.ID, values.logon_message)))

    assert "Password must be between 8 and 30 characters" in error_message.text


@pytest.mark.parametrize(
    "username_input_mismatch, password_input_mismatch",
    [
        ("admin", "UserPass123")
    ]
)


def test_username_password_mismatch(driver, username_input_mismatch, password_input_mismatch):
    # testing password mismatch
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

    error_message = wait.until(EC.visibility_of_element_located((By.ID, values.logon_message)))

    assert "Invalid username or password" in error_message.text


@pytest.mark.parametrize(
    "username_input, password_input_whitespace",
    [
        ("user", " UserPass123"),
        ("user", "UserPass123 ")
    ]
)


def test_username_password_whitespace(driver, username_input, password_input_whitespace):
    # testing password whitespace
    wait = WebDriverWait(driver, 2)
    driver.get(values.site)

    # Input the parameterized username
    username = wait.until(EC.visibility_of_element_located((By.ID, values.username_field)))
    username.send_keys(username_input)

    # Input the parameterized password
    password = driver.find_element(By.ID, values.password_field)
    password.send_keys(password_input_whitespace)

    login_button = driver.find_element(By.ID, values.signin_button)
    login_button.click()

    error_message = wait.until(EC.visibility_of_element_located((By.ID, values.logon_message)))

    assert "Invalid username or password" in error_message.text