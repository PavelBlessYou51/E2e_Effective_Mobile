"""The module contains locators from https://www.saucedemo.com/"""

from selenium.webdriver.common.by import By

# Any page title
PAGE_TITLE = (By.CSS_SELECTOR, "span[class='title']")

# Authorization page locators
USER_NAME_FIELD = (By.CSS_SELECTOR, "#user-name")
PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")

# Products page locators
PRODUCT_ITEMS = (By.CSS_SELECTOR, "div[class='inventory_item']")
ITEM_NAME = "div[class='inventory_item_name ']"
ITEM_PRICE = "div[class='inventory_item_price']"
ADD_BUTTON = "#add-to-cart-sauce-labs-backpack"
CART_BUTTON = (By.CSS_SELECTOR, "a[class='shopping_cart_link']")

# Cart page locators
CART_ITEM_NAME = (By.CSS_SELECTOR, "div[class='inventory_item_name']")
CART_ITEM_PRICE = (By.CSS_SELECTOR, "div[class='inventory_item_price']")
CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkout")

# Checkout: Information page locators
FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#first-name")
LAST_NAME_FIELD = (By.CSS_SELECTOR, "#last-name")
POSTAL_CODE_FIELD = (By.CSS_SELECTOR, "#postal-code")
CONTINUE_BUTTON = (By.CSS_SELECTOR, "#continue")

# Checkout: Overview page locators
FINISH_BUTTON = (By.CSS_SELECTOR, "#finish")

# Checkout: Complete page locators
FINISH_BUTTON = (By.CSS_SELECTOR, "h2[class='complete-header']")