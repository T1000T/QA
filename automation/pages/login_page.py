from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import values
from config.settings import BASE_URL

wait_time = 5


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)

    def open(self):
        self.driver.get(BASE_URL)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def enter_username(self, username):
        username_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, values.username_field)
            )
        )
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, values.password_field)
            )
        )
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, values.signin_button)
            )
        )
        login_button.click()

    def click_forgot_password(self):
        forgot_password_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, values.forgot_button)
            )
        )
        forgot_password_button.click()

    def get_message(self):
        message = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, values.logon_message)
            )
        )
        return message.text