import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    ''' fixture that return a web driver instance with yield to be used by any test_ pytest file
    :return: None
    '''

    # getting driver from driver manager
    _driver = webdriver.Chrome(ChromeDriverManager().install())

    # implicit wait just works for first page loading
    _driver.implicitly_wait(10)

    # returning driver for each test
    yield _driver

    # terminating driver execution
    _driver.quit()
