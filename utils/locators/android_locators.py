from selenium.webdriver.common.by import By
from utils.data import TestData
from appium.webdriver.common.appiumby import AppiumBy

class CommonLocator(object):
    MENU_BUTTON = (By.ID, "com.saucelabs.mydemoapp.android:id/menuIV")

class MenuLocator(object):
    CATALOG_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Catalog\"")
    DRAWING_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Drawing\")")
    LOGIN_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Log In\")")

class LoginPageLocator(object):
    USERNAME_INPUT = (By.ID, "com.saucelabs.mydemoapp.android:id/nameET")
    PASSWORD_INPUT = (By.ID, "com.saucelabs.mydemoapp.android:id/passwordET")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Tap to login with given credentials")

    # @classmethod
    # def select_country(cls, country):
    #     return cls.COUNTRY[1].format(country)
    #
    # @classmethod
    # def select_gender(cls, gender):
    #     return cls.GENDER[1].format(gender)


class HomePageLocator(object):
    PRODUCT_ADD_TO_CART = (
        By.XPATH,
        "//android.widget.TextView[@text='{}']/parent::android.widget.LinearLayout//android.widget.TextView["
        "@text='ADD TO CART']",
    )

    CART_BUTTON = (By.ID, "com.androidsample.generalstore:id/appbar_btn_cart")
    CART_TITLE = (By.XPATH, "//android.widget.TextView[@text='Cart']")
    PRODUCT_NAME = (By.ID, "com.androidsample.generalstore:id/productName")
    PRODUCT_PRICE = (By.ID, "com.androidsample.generalstore:id/productPrice")
    TOTAL_AMOUNT = (By.ID, "com.androidsample.generalstore:id/totalAmountLbl")
    TERMS_AND_CONDITIONS_BUTTON = (
        By.ID,
        "com.androidsample.generalstore:id/termsButton",
    )
    TERMS_AND_CONDITIONS_BUTTON_TITLE = (
        By.ID,
        "com.androidsample.generalstore:id/alertTitle",
    )
    CHECKBOX = (By.CLASS_NAME, "android.widget.CheckBox")
    PROCEED_BUTTON = (By.ID, "com.androidsample.generalstore:id/btnProceed")

    @classmethod
    def product_add_to_cart(cls, product_name):
        return cls.PRODUCT_ADD_TO_CART[1].format(product_name)
