from locators.main_locators import MainLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    main_locators = MainLocators()

    def logout(self):
        self.clik_to_element(self.main_locators.BURGER_MENU)
        self.clik_to_element(self.main_locators.LOGOUT)

    def select(self, value):
        locator = self.main_locators.SELECT
        self.select_by_value(locator=locator, value=value)

    def get_price(self):
        lst = self.are_visible(self.main_locators.PRICE_VALUE)
        lst_price = [i.text for i in lst]
        return lst_price

    def check_filter(self, value):
        self.select(value)
        lst = self.get_price()
        return lst

    def add_to_card(self):
        self.clik_to_element(self.main_locators.SAUCE_LABS_BACKPACK)
        value = self.is_visible(self.main_locators.COUNT_ITEMS)
        return value

    def remove_from_card(self):
        self.clik_to_element(self.main_locators.REMOVE_SAUCE_LABS_BACKPACK)

    def check_elem_is_not_present(self):
        return self.is_invisible(self.main_locators.COUNT_ITEMS)






