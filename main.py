from selenium import webdriver
from pages.HomePage import HomePage
from pages.CartPage import CartPage
from pages.SearchPage import SearchPage


class ThemeBubbleTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://themebubble.com"
        self.test_home_page()
        self.driver.implicitly_wait(10)
        self.test_search_page()
        self.test_cart_page()
        self.tear_down()

    def test_home_page(self):
        self.driver.get(f"{self.base_url}/demo/webify/furniture-shop/")
        home_page = HomePage(self.driver)

        home_page.is_title_matches()
        home_page.is_banner_present()
        home_page.is_site_logo_present()
        home_page.test_search_form("baltimore")

    def test_search_page(self):
        search_page = SearchPage(self.driver)

        search_page.is_matches_title("Baltimore Chair")
        search_page.test_result_price()
        search_page.test_result_product_has_right_colors()
        search_page.test_related_products("Morning Glory", "£45.00")

    def test_cart_page(self):
        self.driver.get(f"{self.base_url}/demo/webify/furniture-shop/cart/")
        cart_page = CartPage(self.driver)

        cart_page.is_title_matches()
        cart_page.is_cart_empty()

    def tear_down(self):
        self.driver.close()


if __name__ == "__main__":
    ThemeBubbleTest()
