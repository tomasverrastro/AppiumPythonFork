import datetime
import inspect
import time
from pathlib import Path

from appium.webdriver import WebElement
from seleniumpagefactory.Pagefactory import PageFactory
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.locators.android_locators import *
from utils.common import get_logger
from utils.data import TestData


class ProductsPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.products_page_locator = ProductsPageLocator

    def get_products_page_title(self):
        driver = self.driver
        log = get_logger()
        return driver.find_element(*self.products_page_locator.PAGE_TITLE_TEXT).text



        driver.find_element(*self.login_locator.PASSWORD_INPUT).send_keys(password)
        driver.hide_keyboard()
        driver.find_element(*self.login_locator.LOGIN_BUTTON).click()
        log.info("Successfully Logged In")



