from conftest import driver
from pageobjects.DuckDuckGo import DuckDuckGO


def test_search_expression(driver):
    search_expression = "python3"
    duck_duck_go = DuckDuckGO(driver)
    duck_duck_go.type_search_expression(search_expression)
    duck_duck_go.click_search_button()

    assert search_expression in duck_duck_go.get_current_url()
