from pageobjects.DuckDuckGo import DuckDuckGO


def test_search_expression(driver):
    search_expression = "python3"
    obj = DuckDuckGO(driver)
    obj.type_search_expression(search_expression)
    obj.click_search_button()
    assert search_expression in obj.get_current_url()
