"""The module contains fixtures for test functions"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import faker


@pytest.fixture()
def driver() -> WebDriver:
    """Creates, opens, returns and closes the browser window"""
    options = Options()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    # driver.quit()

@pytest.fixture(autouse=True)
def setup_teardown_message():
    """Informs about start and finish of testing"""
    print("Start testing!")
    yield
    print("End testing!")

@pytest.fixture()
def give_fake_data() -> tuple[str, str, str]:
    fake_obj = faker.Faker(['en_US'])
    first_name = fake_obj.first_name()
    last_name = fake_obj.last_name()
    postal_code = fake_obj.postalcode()
    return first_name, last_name, postal_code