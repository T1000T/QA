import pytest
from test_data.login_data import *

# out of boundaries
@pytest.mark.negative
@pytest.mark.parametrize("username_input_boundary, password_input_boundary", out_of_boundaries)

def test_username_password_out_of_boundaries(login_page, username_input_boundary, password_input_boundary):
    login_page.open()
    login_page.login(username_input_boundary,password_input_boundary)

    message = login_page.get_message()

    assert "Username must be between 3 and 20 characters" in message or "Password must be between 8 and 30 characters" in message

# short/long password
@pytest.mark.negative
@pytest.mark.parametrize("username_input_length, password_input_length", password_length)

def test_password_length(login_page, username_input_length, password_input_length):
    login_page.open()
    login_page.login(username_input_length, password_input_length)

    message = login_page.get_message()

    assert "Password must be between 8 and 30 characters" in message

# password mismatch
@pytest.mark.negative
@pytest.mark.parametrize("username_input_mismatch, password_input_mismatch", mismatch_credentials)

def test_username_password_mismatch(login_page, username_input_mismatch, password_input_mismatch):
    login_page.open()
    login_page.login(username_input_mismatch, password_input_mismatch)

    message = login_page.get_message()

    assert "Invalid username or password" in message

# empty field
@pytest.mark.negative
@pytest.mark.parametrize("test_username, test_password", empty_data)

def test_login_requires_username_and_password(login_page, test_username, test_password):
    login_page.open()
    login_page.login(test_username, test_password)

    message = login_page.get_message()

    assert "Username and password are required" in message

# locked user
@pytest.mark.negative
@pytest.mark.parametrize("locked_username_input, locked_password_input", locked_user)

def test_locked_user(login_page, locked_username_input, locked_password_input):
    login_page.open()
    login_page.login(locked_username_input, locked_password_input)

    message = login_page.get_message()

    assert "This account is locked. Please contact support" in message

# case-sensitive
@pytest.mark.negative
@pytest.mark.parametrize("casesensitive_username_input, casesensitive_password_input", casesensitive)

def test_username_and_password_are_case_sensitive(login_page, casesensitive_username_input, casesensitive_password_input):
    login_page.open()
    login_page.login(casesensitive_username_input, casesensitive_password_input)

    message = login_page.get_message()

    assert "Invalid username or password" in message

# password whitespace
@pytest.mark.negative
@pytest.mark.parametrize("username_input, password_input_whitespace", password_whitespace)

def test_password_whitespace(login_page, username_input, password_input_whitespace):
    login_page.open()
    login_page.login(username_input, password_input_whitespace)

    message = login_page.get_message()

    assert "Invalid username or password" in message