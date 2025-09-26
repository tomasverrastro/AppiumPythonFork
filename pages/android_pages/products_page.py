import datetime
import inspect
import time
from pathlib import Path

from appium.webdriver import WebElement
from seleniumpagefactory.Pagefactory import PageFactory
from pages.android_pages.home_page import HomePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.android_pages.home_page import HomePage
from utils.locators.android_locators import *
from utils.common import get_logger
from utils.data import TestData


class ProductsPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.products_page_locator = ProductsPageLocator
        self.home_page = HomePage(driver)


    def get_products_page_title(self):
        driver = self.driver
        log = get_logger()
        return driver.find_element(*self.products_page_locator.PAGE_TITLE_TEXT).text

    def press_product(self, product):
        self.scroll_to_element("description", product).click()


    def get_all_product_titles(self):
        """
        Get all product titles by scrolling through the entire list

        Returns:
            list: Complete list of all product titles
        """
        all_titles = []  # Equivalente a ArrayList<String>
        previous_size = 0
        log = get_logger()

        while True:
            # Get currently visible product titles
            visible_products = self.driver.find_elements(*self.products_page_locator.VISIBLE_PRODUCT_TITLES)

            for product in visible_products:
                title = product.text
                if title not in all_titles:  # Avoid duplicates but maintain product order
                    all_titles.append(title)

            # Check if there are new products
            if len(all_titles) == previous_size:
                break  # No new products found, stop scrolling

            previous_size = len(all_titles)
            self.home_page.scroll_down()

        log.info(f"Complete obtained product list: {all_titles}")
        print(f"Complete obtained product list: {all_titles}")
        return all_titles

    def get_all_product_prices(self):
        """
        Get all product prices by scrolling through the entire list

        Returns:
            list: Complete list of all product prices as floats
        """
        prices = []  # Equivalente a ArrayList<Double>
        previous_size = 0
        log = get_logger()

        while True:
            # Get currently visible product prices
            visible_price_elements = self.driver.find_elements(*self.home_locator.PRODUCT_PRICE)

            # Add visible prices with no duplicates
            for price_element in visible_price_elements:
                price_text = price_element.text.replace("$ ", "")  # Remove "$ " prefix
                try:
                    price = float(price_text)  # Convert to float (equivalent to Double.parseDouble)

                    # Avoid duplicates if it's already in the list
                    if price not in prices:
                        prices.append(price)

                except ValueError as e:
                    log.warning(f"Could not parse price: '{price_text}' - {str(e)}")
                    continue

            # Check if there are new products
            if len(prices) == previous_size:
                break  # No new products, finish scroll

            previous_size = len(prices)
            self.scroll_down()

        log.info(f"Complete price list: {prices}")
        print(f"Complete price list: {prices}")
        return prices




