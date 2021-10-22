from selenium.webdriver.common.by import By


class HomePageLocators(object):
    """A class for home page locator"""
    HEADER_PROMOTIONAL_BANNER = (By.XPATH, "/html/body/header/div[1]")
    SITE_LOGO = (By.CLASS_NAME, "tb-custom-logo")


class CartPageLocators(object):
    CART_EMPTY_PARAGRAPH = (By.XPATH, "/html/body/div[4]/div[2]/div/div/div/p[1]")
