from selenium.webdriver.common.by import By


class MainPageLocators():
    pass
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, 'button[value="Log In"]')
    REGISTRATION_FORM = (By.CSS_SELECTOR, 'button[value="Register"]')


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_COST = (By.CSS_SELECTOR, ".col-sm-6.product_main  p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main :nth-child(1)")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner :first-child")
    ADDED_TO_CART_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    CART_COST = (By.CSS_SELECTOR, ".alert-info .alertinner :nth-last-child(1)")
