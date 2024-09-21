"""The module contains basic methods for working with pages"""

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = 'https://www.saucedemo.com/'

    def open(self):
        """Opens the page"""
        self.driver.get(self.url)

    # Methods for seeking elements on the web-page
    def element_is_visible(self, locator: tuple[str, str], timeout: int = 5) -> WebElement:
        """Checks the visibility of an element on the page"""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator: tuple[str, str], timeout: int = 5) -> list[WebElement]:
        """Checks the visibility of an elements on the page"""
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_clickable(self, locator: tuple[str, str], timeout: int = 5) -> WebElement:
        """Checks the clickability of the button"""
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
