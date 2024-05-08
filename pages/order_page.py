from locators.card_locators import CardLocators
from locators.main_locators import MainLocators
from locators.order_locators import OrderLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    order_locators = OrderLocators()
    main_locators = MainLocators()
    card_locators = CardLocators()

    def order_with_valid_credential(self, lst_data):
        self.add_card_to_card()
        self.fill_field(lst_data[0], lst_data[1], lst_data[2])
        self.clik_to_element(self.order_locators.FINISH_BTN_1)
        return self.get_text(self.order_locators.THANK_TEXT)
    def order_with_wrong_credential(self, lst_data):
        self.add_card_to_card()
        self.fill_field(lst_data[0], lst_data[1], lst_data[2])
        return self.get_text(self.order_locators.ERROR_MESSAGE)

    def add_card_to_card(self):
        self.clik_to_element(self.main_locators.SAUCE_LABS_BACKPACK)
        self.clik_to_element(self.main_locators.CART_BTN)
        self.clik_to_element(self.card_locators.CHECKOUT_BTN)
        a = self.get_text(self.main_locators.CART_BTN)
        print(a)

    def fill_field(self, first_name, last_name, zip):
        self.is_visible(self.order_locators.FIRST_NAME).send_keys(first_name)
        self.is_visible(self.order_locators.lAST_NAME).send_keys(last_name)
        self.is_visible(self.order_locators.ZIP).send_keys(zip)
        self.is_clickable(self.order_locators.FINISH_BTN).click()
