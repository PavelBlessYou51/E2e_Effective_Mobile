"""The module contains basic methods for working with pages"""
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main_project_dir.locators import locators



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

    def get_page_title(self) -> str:
        """Gets title of page"""
        elem = self.element_is_visible(locators.PAGE_TITLE)
        elem_title = elem.text
        return elem_title

    def go_to_page(self, page: str) -> str:
        """Navigates to the specified page"""
        pages = {
            'cart_page': locators.CART_BUTTON,
            'info_page': locators.CHECKOUT_BUTTON,
            'overview_page': locators.CONTINUE_BUTTON,
            'finish_page': locators.FINISH_BUTTON
        }
        if page == 'cart_page':
            button = self.element_is_visible(pages[page])
        else:
            button = self.element_is_clickable(pages[page])
        button.click()
        result = self.get_page_title()
        return result

    @staticmethod
    def get_product_attributes(element:  WebElement, attr_name: str) -> str:
        """Gets name or price of product"""
        type_attr = {
            'name': locators.ITEM_NAME,
            'price': locators.ITEM_PRICE
        }
        item_attr = element.find_element(by=By.CSS_SELECTOR, value=type_attr[attr_name]).text
        return item_attr
