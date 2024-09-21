"""The module contains methods for authorization"""
import random
from .base_page import BasePage
from main_project_dir.locators import locators


class LoginPage(BasePage):

    def login_user(self, login: str = 'standard_user', password: str = 'secret_sauce'):
        login_field = self.element_is_visible(locators.USER_NAME_FIELD)
        login_field.send_keys(login)
        pass_field = self.element_is_visible(locators.PASSWORD_FIELD)
        pass_field.send_keys(password)
        self.element_is_clickable(locators.LOGIN_BUTTON).click()


class ProductsPage(BasePage):

    def add_random_item(self) -> tuple[str, str]:
        items = self.elements_are_visible(locators.PRODUCT_ITEMS)
        random_item = random.choice(items)
        item_name = self.get_product_attributes(random_item, 'name')
        item_price = self.get_product_attributes(random_item, 'price')
        return item_name, item_price
