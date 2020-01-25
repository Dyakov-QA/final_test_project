from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        basket.click()

    def should_item_name_match(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        added_item_name = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME).text
        assert item_name == added_item_name, "The item name is not match"

    def should_item_price_match(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        added_item_price = self.browser.find_element(*ProductPageLocators.ADDED_ITEM_PRICE).text
        assert item_price == added_item_price, "The item price is not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
