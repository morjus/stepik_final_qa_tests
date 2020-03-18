from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators
import math
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_to_cart(self):
        # self.should_not_be_success_message()
        add_to_cart_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
        # self.solve_quiz_and_get_code()
        # self.should_see_success_message()
        # self.name_of_product_equal_to_name_in_success_message()
        # self.cost_of_product_equal_to_cart_cost()

    def should_see_success_message(self):
        assert self.is_element_present(
            *ProductPageLocators.ADDED_TO_CART_MESSAGE), "No success message."

    def name_of_product_equal_to_name_in_success_message(self):
        name_of_product = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        name_in_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        assert name_of_product == name_in_message, f'"{name_of_product}" not equal to "{name_in_message}" in success message.'

    def cost_of_product_equal_to_cart_cost(self):
        cost = self.browser.find_element(
            *ProductPageLocators.PRODUCT_COST).text
        result_cost = self.browser.find_element(
            *ProductPageLocators.CART_COST).text
        assert cost == result_cost, f'Result cost: "{result_cost}" in basket not equal to cost of product: "{cost}".'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_CART_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            "Login link is not presented"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_TO_CART_MESSAGE), \
            "Success message is presented, but should disappear"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
