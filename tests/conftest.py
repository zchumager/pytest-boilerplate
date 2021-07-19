import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # implicit wait just works for first page loading
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
