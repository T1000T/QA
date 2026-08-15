import pytest
from automation.test_data.login_data import *

# successful_login
@pytest.mark.positive
@pytest.mark.parametrize("username_input, password_input", successful_login)


def test_successful_login(login_page, username_input, password_input):
    login_page.open()
    login_page.login(username_input, password_input)
    login_page.click_login()

    message = login_page.get_message()

    assert "Login successful" in message


# locked user
@pytest.mark.positive
@pytest.mark.parametrize("locked_username_input, locked_password_input", locked_user)

def test_locked_user(login_page, locked_username_input, locked_password_input):
    login_page.open()
    login_page.login(locked_username_input, locked_password_input)
    message = login_page.get_message()

    assert "This account is locked. Please contact support" in message


# case-sensitive
@pytest.mark.positive
@pytest.mark.parametrize("casesensitive_username_input, casesensitive_password_input", casesensitive)


def test_username_and_password_are_case_sensitive(login_page, casesensitive_username_input, casesensitive_password_input):
    login_page.open()
    login_page.login(casesensitive_username_input, casesensitive_password_input)
    login_page.click_login()

    message = login_page.get_message()

    assert "Invalid username or password" in message


# empty field
@pytest.mark.positive
@pytest.mark.parametrize("test_username, test_password", empty_data)

def test_login_requires_username_and_password(login_page, test_username, test_password):
    # empty username or password
    login_page.open()
    login_page.login(test_username, test_password)
    login_page.click_login()

    message = login_page.get_message()

    assert "Username and password are required" in message


@pytest.mark.positive
# Verify that clicking Forgot Password displays the reset confirmation
def test_forgot_password(login_page):
    login_page.open()
    login_page.click_forgot_password()

    message = login_page.get_message()

    assert "Password reset instructions have been sent." in message
