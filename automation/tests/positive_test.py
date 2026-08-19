import pytest
from test_data.login_data import *

# successful_login
@pytest.mark.positive
@pytest.mark.parametrize("username_input, password_input", successful_login)

def test_successful_login(login_page, username_input, password_input):
    login_page.open()
    login_page.login(username_input, password_input)

    message = login_page.get_message()

    assert "Login successful" in message

# Verify that clicking Forgot Password displays the reset confirmation
@pytest.mark.positive
def test_forgot_password(login_page):
    login_page.open()
    login_page.click_forgot_password()

    message = login_page.get_message()

    assert "Password reset instructions have been sent." in message
