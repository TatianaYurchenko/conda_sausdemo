from datetime import datetime
import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait



@pytest.fixture
def driver():
    chrom_options = webdriver.ChromeOptions()
    chrom_options.add_argument("--incognito")
    chrom_options.add_argument("--window-size=1440,1080")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrom_options)
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today}",     attachment_type=allure.attachment_type.PNG)
    driver.quit()
