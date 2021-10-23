from selenium.webdriver.common.by import By


class HomePageLocators(object):
    """A class for home page locator"""

    HEADER_PROMOTIONAL_BANNER = (By.CLASS_NAME, "tb-promotion-bar")
    SITE_LOGO = (By.CLASS_NAME, "tb-custom-logo")
    SEARCH_ICON = (By.CLASS_NAME, "tb-search-modal-btn")
    SEARCH_INPUT = (By.NAME, "s")


class CartPageLocators(object):
    """A class for cart page locators"""

    CART_EMPTY_PARAGRAPH = (By.CLASS_NAME, "cart-empty")


class SearchPageLocators(object):
    """A class for product price locators"""

    PRODUCT_PRICE = (By.CLASS_NAME, "woocommerce-Price-amount")
    RELATED_PRODUCTS = (By.CLASS_NAME, "tb-section-heading")
    COLOR_SELECT = (By.ID, "pa_color")
    COLOR_OPTIONS = (By.TAG_NAME, "option")
    RELATED_PRODUCTS_CONTAINER = (By.CLASS_NAME, "tb-products")
    SPECIFIC_RELATED_PRODUCT_NAME = (By.XPATH, '//*[@id="product-9"]/div/div[3]/section/div[4]/div/div[4]/div/div['
                                               '3]/h2/a')
    SPECIFIC_RELATED_PRODUCT_PRICE = (By.XPATH, '//*[@id="product-9"]/div/div[3]/section/div[4]/div/div[4]/div/div['
                                                '3]/span/span/bdi')
