"""This module contains DDGSearchPage,
the page object for the DDG search page"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPage:
    # URL

    URL = 'https://www.duckduckgo.com'

    # Add Locator as CLASS VARIABLES bc we really only need one instance of this tuple on the class
    SEARCH_INPUT = (By.ID, 'searchbox_input')

    def __init__(self, browser):
        self.browser = browser

    # Interaction methods
    # Load url
    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)

    # The return key will essentially commit that search and then proceed to start loading the search results page.
