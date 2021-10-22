from selenium import webdriver
from pages.HomePage import HomePage
from pages.CartPage import CartPage


class ThemeBubbleTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://themebubble.com"
        self.test_home_page()
        self.test_cart_page()
        self.tear_down()

    def test_home_page(self):
        self.driver.get(f"{self.base_url}/demo/webify/furniture-shop/")
        home_page = HomePage(self.driver)

        home_page.is_title_matches()
        home_page.is_banner_present()
        home_page.is_site_logo_present()

    def test_cart_page(self):
        self.driver.get(f"{self.base_url}/demo/webify/furniture-shop/cart/")
        cart_page = CartPage(self.driver)

        cart_page.is_title_matches()
        cart_page.is_cart_empty()

    def tear_down(self):
        self.driver.close()


if __name__ == "__main__":
    ThemeBubbleTest()
