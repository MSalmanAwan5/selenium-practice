from pages.BasePage import BasePage


class CartPage(BasePage):
    """Home page tests come in this class"""

    def is_title_matches(self):
        """Verifies that the hardcoded text "Home - Furniture Shop" appears in page title"""

        return "Cart - Furniture Shop" in self.driver.title

    def is_cart_empty(self):
        """Verifies that the cart is empty"""
        assert "Your cart is currently empty." in self.driver.page_source
