from pages.BasePage import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):
    """Home page tests come in this class"""

    def is_title_matches(self):
        """Verifies that the hardcoded text "Home - Furniture Shop" appears in page title"""

        return "Cart - Furniture Shop" in self.driver.title

    def is_cart_empty(self):
        """Verifies that the cart is empty"""

        cart_empty_text = self.driver.find_element(*CartPageLocators.CART_EMPTY_PARAGRAPH).text
        assert "Your cart is currently empty." == cart_empty_text
