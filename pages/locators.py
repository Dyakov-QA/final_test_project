from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADDED_ITEM_NAME = (By.CSS_SELECTOR, ".alert-success strong")

    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    ADDED_ITEM_PRICE = (By.CSS_SELECTOR, ".alert-info strong")

