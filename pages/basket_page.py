from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    
    def should_see_message_about_nothing_in_basket(self):
        #print(self.browser.find_element(*BasketPageLocators.MESSAGE_ABOUT_EMPTY).text)
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.MESSAGE_ABOUT_EMPTY).text, "No message about empty."
        '''assert self.is_element_present(
            *BasketPageLocators.MESSAGE_ABOUT_EMPTY), \
                "Basket is not empty!"'''

    def should_see_nothing_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.CHECKOUT_BUTTON), \
            "Checkout button is presented, but should not be"