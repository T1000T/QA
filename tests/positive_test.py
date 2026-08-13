import values
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# successful_login
@pytest.mark.parametrize(
    "username_input, password_input",
    [
        ("admin", "Password123"),
        (" admin", "Password123"),
        ("admin ", "Password123"),
        ("user", "UserPass123")
    ]
)


def test_successful_login(driver, username_input, password_input):
    # testing multiple successful logins
    wait = WebDriverWait(driver, 5)
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
    assert "Login successful" in success_message.text


# locked user
@pytest.mark.parametrize(
    "locked_username_input, locked_password_input",
    [
        ("locked", "Locked123")
    ]
)

def test_locked_user(driver, locked_username_input, locked_password_input):
    # testing locked user
    wait = WebDriverWait(driver, 5)
    driver.get(values.site)

    # Input the parameterized username
    username = wait.until(EC.visibility_of_element_located((By.ID, values.username_field)))
    username.send_keys(locked_username_input)

    # Input the parameterized password
    password = driver.find_element(By.ID, values.password_field)
    password.send_keys(locked_password_input)

    login_button = driver.find_element(By.ID, values.signin_button)
    login_button.click()

    error_message = wait.until(EC.visibility_of_element_located((By.ID, values.logon_message)))

    assert "This account is locked. Please contact support" in error_message.text


# case-sensitive
@pytest.mark.parametrize(
    "casesensitive_username_input, casesensitive_password_input",
    [
        ("Admin", "Password123"),
        ("ADMIN", "Password123"),
        ("admin", "password123"),
        ("admin", "PASSWORD123")
        ]
)

def test_casesensitive_user_password(driver, casesensitive_username_input, casesensitive_password_input):
    # testing locked user
    wait = WebDriverWait(driver, 5)
    driver.get(values.site)

    # Input the parameterized username
    username = wait.until(EC.visibility_of_element_located((By.ID, values.username_field)))
    username.send_keys(casesensitive_username_input)

    # Input the parameterized password
    password = driver.find_element(By.ID, values.password_field)
    password.send_keys(casesensitive_password_input)

    login_button = driver.find_element(By.ID, values.signin_button)
    login_button.click()

    error_message = wait.until(EC.visibility_of_element_located((By.ID, values.logon_message)))

    assert "Invalid username or password" in error_message.text


# empty field
@pytest.mark.parametrize(
    "test_username, test_password",
    [
        ("", "Password123"),
        ("admin", ""),
    ]
)


def test_empty_username_password(driver, test_username, test_password):
    # testing locked user
    wait = WebDriverWait(driver, 5)
    driver.get(values.site)

    # Input the parameterized username
    username = wait.until(EC.visibility_of_element_located((By.ID, values.username_field)))
    username.send_keys(test_username)

    # Input the parameterized password
    password = driver.find_element(By.ID, values.password_field)
    password.send_keys(test_password)

    login_button = driver.find_element(By.ID, values.signin_button)
    login_button.click()

    error_message = wait.until(EC.visibility_of_element_located((By.ID, values.logon_message)))

    assert "Username and password are required" in error_message.text


def test_forgot_password(driver):
    # testing locked user
    wait = WebDriverWait(driver, 5)
    driver.get(values.site)

    login_button = driver.find_element(By.ID, values.forgot_button)
    login_button.click()

    error_message = wait.until(EC.visibility_of_element_located((By.ID, values.logon_message)))

    assert "Password reset instructions have been sent." in error_message.text
