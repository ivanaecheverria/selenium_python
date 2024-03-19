"""This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search resultpage"""
from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:

    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    #Initializer
    def __init__(self, browser):
        self.browser = browser

    #Interaction Methods
    #should return a list of all link titles for the result
    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles
#we don't want to get a list of elements, but a list of strings containing the titles
    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value
#should get the text value of my search input field from the result page
    def title(self):
        return self.browser.title