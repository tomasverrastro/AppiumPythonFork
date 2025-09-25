from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

class CommonLocator(object):
    MENU_BUTTON = (By.ID, "com.saucelabs.mydemoapp.android:id/menuIV")
    CART_BUTTON = (By.ID, "com.saucelabs.mydemoapp.android:id/cartRL")
    SORT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Shows current sorting order and displays available sorting options")
    DESCENDING_NAME_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Descending order by name")
    ASCENDING_PRICE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Descending order by name")

class MenuLocator(object):
    CATALOG_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Catalog\"")
    DRAWING_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Drawing\")")
    LOGIN_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Log In\")")
    RESET_APP_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Reset App State\")")
    CONFIRM_RESET_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"android:id/button1\")")
    SUCCESSFUL_RESET_TEXT = (AppiumBy.ANDROID_UIAUTOMATOR,  "new UiSelector().resourceId(\"android:id/message\")")
    OK_SUCCESSFUL_RESET_BUTTON = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().resourceId(\"android:id/button1\")")

class LoginPageLocator(object):
    USERNAME_INPUT = (By.ID, "com.saucelabs.mydemoapp.android:id/nameET")
    PASSWORD_INPUT = (By.ID, "com.saucelabs.mydemoapp.android:id/passwordET")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Tap to login with given credentials")
    REQUIRED_USERNAME_TEXT = (By.ID, "com.saucelabs.mydemoapp.android:id/nameErrorTV")
    REQUIRED_PASSWORD_TEXT = (By.ID, "com.saucelabs.mydemoapp.android:id/passwordErrorTV")

class ProductsPageLocator(object):
    PAGE_TITLE_TEXT = (By.ID, "com.saucelabs.mydemoapp.android:id/productTV")
    VISIBLE_PRODUCT_TITLES = (By.ID, "com.saucelabs.mydemoapp.android:id/titleTV")
    VISIBLE_PRODUCT_PRICES = (By.ID, "com.saucelabs.mydemoapp.android:id/priceTV")

class CartPageLocator(object):
    PAGE_TITLE_TEXT = (By.ID, "com.saucelabs.mydemoapp.android:id/noItemTitleTV")
    REMOVE_ITEM_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Removes product from cart")
    CHECKOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Confirms products for checkout")

class CheckoutPageLocator(object):
    PAGE_TITLE_TEXT = (By.ID, "com.saucelabs.mydemoapp.android:id/checkoutTitleTV")
    FULL_NAME_INPUT = (By.ID, "com.saucelabs.mydemoapp.android:id/fullNameET")
    ADDRESS1_INPUT= (By.ID, "com.saucelabs.mydemoapp.android:id/address1ET")
    CITY_INPUT = (By.ID, "com.saucelabs.mydemoapp.android:id/cityET")
    ZIP_CODE_INPUT = (By.ID, "com.saucelabs.mydemoapp.android:id/zipET")
    COUNTRY_INPUT = (By.ID, "com.saucelabs.mydemoapp.android:id/countryET")
    TO_PAYMENT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Saves user info for checkout")
    ZIP_ERROR_TEXT = (By.ID, "com.saucelabs.mydemoapp.android:id/zipErrorTV")

class CheckoutCompletePageLocator(object):
    CHECKOUT_COMPLETE_TEXT = (By.ID, "com.saucelabs.mydemoapp.android:id/completeTV")
    CONTINUE_SHOPPING_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Tap to open catalog")

class DrawingPageLocator(object):
    DRAWING_PAD = (By.ID, "com.saucelabs.mydemoapp.android:id/signature_pad")
    SAVE_DRAWING_BUTTON = (By.ID, "com.saucelabs.mydemoapp.android:id/saveBtn")
    SUCCESSFUL_SAVE_TEXT = (By.ID, "android:id/message")
    OK_SAVE_DRAWING_BUTTON = (By.ID, "android:id/button1")
    ALLOW_PERMISSION_BUTTON = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")

class OrderReviewPageLocator(object):
    ORDER_REVIEW_TEXT = (By.ID, "com.saucelabs.mydemoapp.android:id/enterShippingAddressTV")
    PLACE_ORDER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Completes the process of checkout")

class PaymentPageLocator(object):
    PAYMENT_METHOD_TEXT = (By.ID, "com.saucelabs.mydemoapp.android:id/enterPaymentMethodTV")
    FULL_NAME_INPUT = (By.ID, "com.saucelabs.mydemoapp.android:id/nameET")
    CARD_NUMBER_INPUT = (By.ID, "com.saucelabs.mydemoapp.android:id/cardNumberET")
    EXPIRATION_DATE_INPUT = (By.ID, "com.saucelabs.mydemoapp.android:id/expirationDateET")
    SECURITY_CODE_INPUT = (By.ID, "com.saucelabs.mydemoapp.android:id/securityCodeET")
    REVIEW_ORDER_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Saves payment info and launches screen to review checkout data")
    SECURITY_CODE_ERROR_TEXT = (By.ID, "com.saucelabs.mydemoapp.android:id/securityCodeErrorTV")

class ProductDetailsPageLocator(object):
    PRODUCT_NAME_TEXT = (By.ID, "com.saucelabs.mydemoapp.android:id/productTV")
    RATE_5_STARS_BUTTON = (By.ID, "com.saucelabs.mydemoapp.android:id/start5IV")
    SUCCESSFUL_REVIEW_TEXT = (By.ID, "com.saucelabs.mydemoapp.android:id/sortTV")
    OK_SUCCESSFUL_REVIEW_BUTTON = (By.ID, "com.saucelabs.mydemoapp.android:id/closeBt")
    CLOSE_REVIEW_DIALOG_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Closes review dialog")
    PRODUCT_PRICE_TEXT = (By.ID, "com.saucelabs.mydemoapp.android:id/priceTV")
    ADD_TO_CART_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Tap to add product to cart")
    PRODUCT_DESCRIPTION_TEXT = (By.ID, "com.saucelabs.mydemoapp.android:id/descTV")
    CART_AMOUNT_TEXT = (By.ID, "com.saucelabs.mydemoapp.android:id/cartTV")



