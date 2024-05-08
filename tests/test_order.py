import time

import allure
import pytest

from pages.order_page import OrderPage
from src.order_data import OrderData
from src.urls import Urls


@allure.epic("Testing order page")
class TestOrder():
    url = Urls()
    data = OrderData()
    def test_order_with_valid_credential(self, driver):
        page = OrderPage(driver, self.url.base_url)
        page.open()
        page.login()
        expected_text = page.order_with_valid_credential(self.data.user_data_with_valid_credential)
        print(expected_text)
        assert self.data.thank_text == expected_text
        time.sleep(1)
    @pytest.mark.parametrize("lst_data", data.user_data)
    def test_order_with_wrong_credential(self, driver, lst_data):
        page = OrderPage(driver, self.url.base_url)
        page.open()
        page.login()
        expected_text = page.order_with_wrong_credential(lst_data)
        print(expected_text)
        assert lst_data[3] == expected_text
        time.sleep(1)
