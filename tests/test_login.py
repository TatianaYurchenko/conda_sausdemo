import allure
import os
from locators.main_locators import MainLocators
from pages.login_page import LoginPage
from src.urls import Urls
from dotenv import load_dotenv
load_dotenv()
@allure.epic("Testing login page")
class TestLogin:
    url = Urls()
    locators = MainLocators()
    base_url = os.getenv("BASE_URL")

    @allure.title('test login')
    @allure.description("тест проверяет что после логинки пользователь попадает на главную страницу")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self, driver):
        page = LoginPage(driver, self.base_url)
        page.open()
        page.login()
        actual_text = page.get_text(self.locators.TITLE)
        expected_text = "Products"
        assert actual_text == expected_text, f"Unexpected text,expected_text {expected_text} actual_text {actual_text}"

    @allure.title('test login1')
    @allure.description("После перехода на главную страницу пользователь видит карточки тиовара")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login_1(self, driver):
        page = LoginPage(driver, self.base_url)
        page.open()
        page.login()
        expected_len = 6
        cards = page.get_length(self.locators.CARDS)
        assert cards == expected_len, f"expected {expected_len} actual {cards}"
