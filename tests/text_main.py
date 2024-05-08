import time

import pytest
import allure

from functions.function import sort_list, replace_value, sort_list_1
from pages.main_page import MainPage
from src.urls import Urls

@allure.epic("Testing main page")
class TestMainPage:
    url = Urls()

    def test_logout(self, driver):
        page = MainPage(driver, self.url.base_url)
        page.open()

        page.login()
        assert driver.current_url == self.url.main_url
        page.logout()
        assert driver.current_url != self.url.main_url

    def test_select(self, driver):
        page = MainPage(driver, self.url.base_url)
        page.open()
        page.login()
        lst = page.check_filter("lohi")
        assert replace_value(lst, "$") == sort_list(lst, False)
        print(replace_value(lst, "$"))
    @pytest.mark.parametrize("value", [["lohi", False], ["hilo", True]])
    def test_select_with_lambda(self, driver, value):
        page = MainPage(driver, self.url.base_url)
        page.open()
        page.login()
        lst = page.check_filter(value[0])
        print()
        print(lst)
        print(sort_list_1(lst, value[1]))
        assert lst == sort_list_1(lst, value[1])

    def test_add_item_to_cart(self, driver):
        page = MainPage(driver, self.url.base_url)
        page.open()
        page.login()
        value = page.add_to_card()
        assert value.text =="1"

    def test_remove_item_from_cart(self, driver):
        page = MainPage(driver, self.url.base_url)
        page.open()
        page.login()
        page.add_to_card()
        page.remove_from_card()
        value = page.check_elem_is_not_present()
        assert value is True
