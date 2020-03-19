from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login = 'login'
        assert login in self.browser.current_url, f'No {login} in {self.browser.current_url}'

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_BUTTON), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_BUTTON), "Login form is not presented"

    def register_new_user(self, email, password):
        email_area = self.browser.find_element(
            *LoginPageLocators.REG_EMAIL_INPUT)
        email_area.click()
        email_area.send_keys(email)

        passw1 = self.browser.find_element(
            *LoginPageLocators.REG_PASSWORD_INPUT)
        passw1.click()
        passw1.send_keys(str(password))

        passw2 = self.browser.find_element(
            *LoginPageLocators.REG_REPEAT_PASSWORD)
        passw2.click()
        passw2.send_keys(str(password))

        reg_button = self.browser.find_element(
            *LoginPageLocators.REGISTRATION_BUTTON)
        reg_button.click()

        assert not self.is_not_element_present(
            *LoginPageLocators.REGISTRATION_SUCCESSFUL_MESSAGE, timeout=15), "Registration successful message is not presented"
