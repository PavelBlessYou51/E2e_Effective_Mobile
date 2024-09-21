import allure

from main_project_dir.pages.main_page import MainPage
from main_project_dir.tests.conftest import driver

@allure.title("E2E test of buying product")
def test_end_to_end(driver, give_fake_data):
    main_page = MainPage(driver)
    main_page.open()
    with allure.step("Login the user"):
        login_result = main_page.login_user()
        assert login_result == "Products", "The user didn't login!"
    with allure.step("Adding a random product in the cart and go to the cart"):
        added_item = main_page.add_random_item()
        go_card_result = main_page.go_to_page('cart_page')
        assert go_card_result == "Your Cart", "The user didn't go to the cart page!"
    with allure.step("Checking the added item in the cart"):
        item_in_cart = main_page.check_added_item()
        count_added_item = main_page.get_count_added_items()
        assert len(count_added_item) == 1, "There is more then one item in the cart!"
        assert added_item == item_in_cart, "There is wrong item in the cart!"
    with allure.step("Go to 'Checkout: Your Information' page"):
        go_info_page_result = main_page.go_to_page('info_page')
        assert  go_info_page_result == "Checkout: Your Information", "The user didn't go to 'Checkout: Your Information' page!"
    with allure.step("Filling the customer form and go to 'Checkout: Overview' page"):
        main_page.fill_person_data(*give_fake_data)
        go_overview_page_result = main_page.go_to_page('overview_page')
        assert go_overview_page_result == "Checkout: Overview", "The user didn't go to 'Checkout: Overview' page!"
    with allure.step("Checking the added item on 'Checkout: Overview' page"):
        item_in_overview = main_page.check_added_item()
        count_items_in_overview = main_page.get_count_added_items()
        assert len(count_items_in_overview) == 1, "There is more then one item in the overview!"
        assert item_in_cart == item_in_overview, "There is wrong item in the overview!"
    with allure.step("Going to the finish page and getting confirmation of order"):
        go_complete_result = main_page.go_to_page('finish_page')
        confirmation = main_page.get_confirm_order()
        assert go_complete_result == "Checkout: Complete!", "The user didn't go to 'Checkout: Complete!' page!"
        assert confirmation == "Thank you for your order!", "The order confirmation has not been received"
