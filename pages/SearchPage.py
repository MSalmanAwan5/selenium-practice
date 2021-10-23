from pages.BasePage import BasePage
from pages.locators import SearchPageLocators


class SearchPage(BasePage):
    """Search page tests come in this class"""

    def is_matches_title(self, product_name):
        f"""Verifies that the hardcoded text "{product_name} - Furniture Shop" appears in page title"""

        assert f"{product_name} - Furniture Shop" in self.driver.title

    def test_result_price(self):
        """Verifies that the result product price is correct and displayed"""

        price_text = self.driver.find_element(*SearchPageLocators.PRODUCT_PRICE).text
        assert "£15.00" == price_text

    def test_result_product_has_right_colors(self):
        """Verifies that the result product has colors Blue / Green and Red"""

        color_options_to_match = ["", "blue", "green", "red"]

        color_select_element = self.driver.find_element(*SearchPageLocators.COLOR_SELECT)
        color_options = color_select_element.find_elements(*SearchPageLocators.COLOR_OPTIONS)

        # check if both lists are equal regardless of order
        assert set([color.get_attribute("value") for color in color_options]) == set(color_options_to_match)

    def test_related_products(self, product_name, price):
        """Verifies that related products section is visible"""

        related_products_heading = self.driver.find_element(*SearchPageLocators.RELATED_PRODUCTS)
        assert related_products_heading.is_displayed()
        assert related_products_heading.text == "Related products"
        specific_product_element_name = self.driver.find_element(*SearchPageLocators.SPECIFIC_RELATED_PRODUCT_NAME)
        specific_product_element_price = self.driver.find_element(*SearchPageLocators.SPECIFIC_RELATED_PRODUCT_PRICE)

        assert product_name == specific_product_element_name.text
        assert price == specific_product_element_price.text
