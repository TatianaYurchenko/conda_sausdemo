import allure
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from dotenv import load_dotenv
from locators.login_locators import LoginLocators
from src.user_data import UserData
import os

load_dotenv()
class BasePage:
    login_locators = LoginLocators()
    user = UserData()
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step("Login")
    def login(self):
        with allure.step("Username"):
            self.is_clickable(self.login_locators.USER_NAME).send_keys(os.getenv("STANDARD_USER"))
        with allure.step("Password"):
            self.is_clickable(self.login_locators.PASSWORD).send_keys(os.getenv("SECRET_SAUCE"))
        with allure.step("Click"):
            self.is_clickable(self.login_locators.LOGIN_BTN).click()

    @allure.step("Open brawser")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Get text")
    def get_text(self, locator):
        return self.is_visible(locator).text

    @allure.step("Get len")
    def get_length(self, locator):
        return len(self.are_visible(locator))

    def clik_to_element(self, locator):
        return self.is_clickable(locator).click()

    def is_visible(self, locator: tuple, timeout: int = 10) -> WebElement:
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def are_visible(self, locator: tuple, timeout: int = 10):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def is_clickable(self, locator: tuple, timeout: int = 10) -> WebElement:
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def select_by_value(self, locator, value):
        select_element = self.driver.find_element(*locator)
        select = Select(select_element)
        select.select_by_value(value)

    def is_invisible(self, locator, timeout: int = 10):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))



