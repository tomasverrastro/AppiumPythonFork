import pytest
import allure
from pages.android_pages.home_page import HomePage
from pages.android_pages.login_page import LoginPage
from pages.android_pages.products_page import ProductsPage
from utils.common import get_test_data


@allure.title("Login & Products Test")
@pytest.mark.usefixtures("setup")
class TestLogin:
    @allure.step("test_correct_login")
    @allure.description("Login with correct credentials")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", get_test_data("info"))
    def test_correct_login(self, data):
        homepage = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        products_page = ProductsPage(self.driver)
        homepage.click_menu_button()
        homepage.click_login_button()
        login_page.fill_login_form(data["email"], data["password"])
        homepage.capture_screenshot()
        assert "Products" in products_page.get_products_page_title()

    @allure.step("test_incorrect_login")
    @allure.description("Login with incorrect sets of data")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", get_test_data("incorrect_login"))
    def test_incorrect_login(self, data):
        homepage = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        products_page = ProductsPage(self.driver)
        homepage.click_menu_button()
        homepage.click_login_button()
        login_page.fill_login_form(data["email"], data["password"])
        homepage.capture_screenshot()
        assert data["text"] in homepage.get_text_from_element(data["element"])


    @allure.step("test_get_products")
    @allure.description("Obtain list of products")
    @pytest.mark.smoke
    def test_get_products(self):
        products_page = ProductsPage(self.driver)
        products_page.get_all_product_titles()




