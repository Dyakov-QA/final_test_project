from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_basket_item(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket item is presented, but should not be"

    def should_be_basket_empty_message(self):
        basket_message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).text
        assert basket_message == "Your basket is empty. Continue shopping", "The 'Your basket is empty' message is'n present"
