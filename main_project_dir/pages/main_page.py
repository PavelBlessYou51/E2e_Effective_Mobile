"""The module contains methods for authorization"""
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from .base_page import BasePage
from main_project_dir.locators import locators


class MainPage(BasePage):

    # Login page
    def login_user(self, login: str = 'standard_user', password: str = 'secret_sauce') -> str:
        login_field = self.element_is_visible(locators.USER_NAME_FIELD)
        login_field.send_keys(login)
        pass_field = self.element_is_visible(locators.PASSWORD_FIELD)
        pass_field.send_keys(password)
        self.element_is_clickable(locators.LOGIN_BUTTON).click()
        login_result = self.get_page_title()
        return login_result

    # Products page
    def add_random_item(self) -> tuple[str, str]:
        items = self.elements_are_visible(locators.PRODUCT_ITEMS)
        random_item = random.choice(items)
        random_item.find_element(by=By.CSS_SELECTOR, value=locators.ADD_BUTTON).click()
        item_name = self.get_product_attributes(random_item, 'name')
        item_price = self.get_product_attributes(random_item, 'price')
        return item_name, item_price

    # Cart page
    def get_count_added_items(self) -> list[WebElement]:
        items = self.elements_are_visible(locators.CART_ITEMS)
        return items

    def check_added_item(self) -> tuple[str, str]:
        item = self.get_count_added_items()
        item_name = self.get_product_attributes(item[0], 'name')
        item_price = self.get_product_attributes(item[0], 'price')
        return item_name, item_price

    # Checkout: Your information page
    def fill_person_data(self, first_name, last_name, postal_code):
        first_name_field = self.element_is_visible(locators.FIRST_NAME_FIELD)
        first_name_field.send_keys(first_name)
        last_name_name_field = self.element_is_visible(locators.LAST_NAME_FIELD)
        last_name_name_field.send_keys(last_name)
        postal_code_field = self.element_is_visible(locators.POSTAL_CODE_FIELD)
        postal_code_field.send_keys(postal_code)

    # Checkout: Complete page
    def get_confirm_order(self) -> str:
        element = self.element_is_visible(locators.ORDER_CONFIRMATION)
        confirmation = element.text
        return confirmation




