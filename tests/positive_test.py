import pytest
from login_page import LoginPage

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
    login_page = LoginPage(driver)

    login_page.open()
    login_page.enter_username(username_input)
    login_page.enter_password(password_input)
    login_page.click_login()

    message = login_page.get_message()

    assert "Login successful" in message


# locked user
@pytest.mark.parametrize(
    "locked_username_input, locked_password_input",
    [
        ("locked", "Locked123")
    ]
)

def test_locked_user(driver, locked_username_input, locked_password_input):
    # testing locked user
    login_page = LoginPage(driver)

    login_page.open()
    login_page.enter_username(locked_username_input)
    login_page.enter_password(locked_password_input)
    login_page.click_login()

    message = login_page.get_message()

    assert "This account is locked. Please contact support" in message


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

def test_username_and_password_are_case_sensitive(driver, casesensitive_username_input, casesensitive_password_input):
    # testing case-sensitive user
    login_page = LoginPage(driver)

    login_page.open()
    login_page.enter_username(casesensitive_username_input)
    login_page.enter_password(casesensitive_password_input)
    login_page.click_login()

    message = login_page.get_message()

    assert "Invalid username or password" in message


# empty field
@pytest.mark.parametrize(
    "test_username, test_password",
    [
        ("", "Password123"),
        ("admin", ""),
    ]
)


def test_login_requires_username_and_password(driver, test_username, test_password):
    # testing empty field
    login_page = LoginPage(driver)

    login_page.open()
    login_page.enter_username(test_username)
    login_page.enter_password(test_password)
    login_page.click_login()

    message = login_page.get_message()

    assert "Username and password are required" in message


def test_forgot_password(driver):
    # Verify that clicking Forgot Password displays the reset confirmation
    login_page = LoginPage(driver)
    login_page.open()

    login_page.click_forgot_password()

    message = login_page.get_message()

    assert "Password reset instructions have been sent." in message
