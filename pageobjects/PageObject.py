from selenium.webdriver.remote.webdriver import WebDriver


class PageObject:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title
