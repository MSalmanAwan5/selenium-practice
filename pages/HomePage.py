from pages.BasePage import BasePage
from pages.locators import HomePageLocators
from selenium.webdriver.common.keys import Keys


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

    def test_search_form(self, search_query):
        """checks if the search form works"""

        search_icon_element = self.driver.find_element(*HomePageLocators.SEARCH_ICON)
        self.driver.implicitly_wait(5)
        search_icon_element.click()
        self.driver.implicitly_wait(5)
        search_input_element = self.driver.find_element(*HomePageLocators.SEARCH_INPUT)
        search_input_element.send_keys(search_query)
        search_input_element.send_keys(Keys.RETURN)
