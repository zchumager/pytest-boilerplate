import pytest
import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    # getting driver from driver manager
    _driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # implicit wait just works for first page loading
    _driver.implicitly_wait(config.DEFAULT_WAIT_TIME)

    # returning driver for each test
    yield _driver

    # terminating driver execution
    _driver.quit()
