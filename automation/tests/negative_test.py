import pytest
from test_data.login_data import *

# out of boundaries
@pytest.mark.negative
@pytest.mark.parametrize("username_input_boundary, password_input_boundary", out_of_boundaries)

def test_username_password_out_of_boundaries(login_page, username_input_boundary, password_input_boundary):
    login_page.open()
    login_page.login(username_input_boundary,password_input_boundary)
    login_page.click_login()

    message = login_page.get_message()

    assert "Username must be between 3 and 20 characters" in message or "Password must be between 8 and 30 characters" in message

# short/long password
@pytest.mark.negative
@pytest.mark.parametrize("username_input_length, password_input_length", password_length)

def test_password_length(login_page, username_input_length, password_input_length):
    login_page.open()
    login_page.login(username_input_length, password_input_length)
    login_page.click_login()

    message = login_page.get_message()

    assert "Password must be between 8 and 30 characters" in message

# password mismatch
@pytest.mark.negative
@pytest.mark.parametrize("username_input_mismatch, password_input_mismatch", mismatch_credentials)

def test_username_password_mismatch(login_page, username_input_mismatch, password_input_mismatch):
    login_page.open()
    login_page.login(username_input_mismatch, password_input_mismatch)
    login_page.click_login()

    message = login_page.get_message()

    assert "Invalid username or password" in message

# password whitespace
@pytest.mark.negative
@pytest.mark.parametrize("username_input, password_input_whitespace", password_whitespace)

@pytest.mark.negative
def test_password_whitespace(login_page, username_input, password_input_whitespace):
    login_page.open()
    login_page.login(username_input, password_input_whitespace)
    login_page.click_login()

    message = login_page.get_message()

    assert "Invalid username or password" in message