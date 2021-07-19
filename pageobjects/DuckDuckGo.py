from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pageobjects.PageObject import PageObject
import config


class DuckDuckGO(PageObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://duckduckgo.com/")
        self.input_id = (By.ID, "search_form_input_homepage")
        self.button_id = (By.ID, "search_button_homepage")

    def type_search_expression(self, text: str):
        WebDriverWait(self.driver, config.DEFAULT_WAIT_TIME)\
            .until(expected_conditions.visibility_of_element_located(self.input_id)).send_keys(text)

    def click_search_button(self):
        WebDriverWait(self.driver, config.DEFAULT_WAIT_TIME)\
            .until(expected_conditions.element_to_be_clickable(self.button_id)).click()
