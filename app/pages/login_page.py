from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.login_locators import LoginLocators
from pages.base_page import BasePage
from config.settings import settings


class LoginPage(BasePage):
    def load(self):
        self.open(settings.ebanca_url)

    def enter_username(self, username: str):
        field = self.find_first_visible(LoginLocators.USERNAME_CANDIDATES)
        self.type_text(field, username)

    def continue_after_username(self):
        button = self.find_first_clickable(LoginLocators.CONTINUE_CANDIDATES)
        self.click(button)

    def wait_for_password_code_field(self):
        return self.find_first_visible(LoginLocators.PASSWORD_CODE)

    def enter_code(self, code: str):
        field = self.wait_for_password_code_field()
        self.type_text(field, code)

    def submit_code(self):
        button = self.find_first_clickable(LoginLocators.CONTINUE_CODE)
        self.click(button)

    def wait_for_password_field(self):
        return self.find_first_visible(LoginLocators.PASSWORD_CANDIDATES)

    def enter_password(self, password: str):

        field = self.find_first_visible(
        LoginLocators.PASSWORD_CANDIDATES
        )

        # Dar foco al campo
        self.driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        field
        )

        field.click()
        # Selenium escribe como teclado, no como pegado
        field.clear()

        field.send_keys(password)

    def submit_login(self):
        button = self.find_first_clickable(LoginLocators.LOGIN_CANDIDATES)
        self.click(button)
