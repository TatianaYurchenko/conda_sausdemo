class OrderLocators:
    FIRST_NAME = ("xpath", '//input[@id="first-name"]')
    lAST_NAME = ("xpath", '//input[@id="last-name"]')
    ZIP = ("xpath", '//input[@id="postal-code"]')
    CONTINUE_BTN = ("xpath", '//input[@id="continue"]')
    FINISH_BTN = ("xpath", '//input[@type="submit"]')
    FINISH_BTN_1 = ("xpath", '//button[@id="finish"]')
    THANK_TEXT = ("xpath", '//h2[@class="complete-header"]')
    ERROR_MESSAGE = ("xpath", '//h3[@data-test="error"]')
