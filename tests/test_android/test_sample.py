import pytest
import allure
from pages.android_pages.home_page import HomePage
from pages.android_pages.login_page import LoginPage
from pages.android_pages.products_page import ProductsPage
from utils.common import get_test_data


@allure.title("Login & Products Test")
@pytest.mark.usefixtures("setup")
class TestHomePage:
    @allure.step("test_fill_form")
    @allure.description("Filling Form with different datasets")
    @pytest.mark.smoke
    @pytest.mark.parametrize("data", get_test_data("info"))
    def test_fill_form(self, data):
        homepage = HomePage(self.driver)
        login_page = LoginPage(self.driver)
        products_page = ProductsPage(self.driver)
        homepage.click_menu_button()
        homepage.click_login_button()
        login_page.fill_login_form(data["email"], data["password"])
        homepage.capture_screenshot()
        assert "Products" in products_page.get_products_page_title()


    @allure.step("test_get_products")
    @allure.description("Obtain list of products")
    @pytest.mark.smoke
    def test_get_products(self):
        products_page = ProductsPage(self.driver)
        products_page.get_all_product_titles()




