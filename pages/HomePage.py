from pages.BasePage import BasePage
from pages.locators import HomePageLocators


class HomePage(BasePage):
    """Home page tests come in this class"""

    def is_title_matches(self):
        """Verifies that the hardcoded text "Home - Furniture Shop" appears in page title"""

        return "Home - Furniture Shop" in self.driver.title

    def is_banner_present(self):
        """checks if the promotional banner is present"""

        return self.driver.find_element(*HomePageLocators.HEADER_PROMOTIONAL_BANNER).is_displayed()

    def is_site_logo_present(self):
        """checks if the site logo is present"""

        return self.driver.find_element(*HomePageLocators.SITE_LOGO).is_displayed()
