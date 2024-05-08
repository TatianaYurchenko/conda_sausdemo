import random


class MainLocators:
    TITLE = ("xpath", "//span[@class='title']")
    CARDS = ("xpath", "//div[@class='inventory_item']")
    SAUCE_LABS_BACKPACK = ("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
    CART_BTN = ("xpath", "//a[@class='shopping_cart_link']")
    BURGER_MENU = ("xpath", '//button[@id="react-burger-menu-btn"]')
    LOGOUT = ("xpath", '//a[@id="logout_sidebar_link"]')
    SELECT = ("xpath", '//select[@class="product_sort_container"]')
    PRICE_VALUE = ("xpath", '//div[@class="inventory_item_price"]')
    COUNT_ITEMS = ("xpath", '//span[@data-test="shopping-cart-badge"]')
    REMOVE_SAUCE_LABS_BACKPACK = ("xpath", '//button[@data-test="remove-sauce-labs-backpack"]')




