from pageobjects.DuckDuckGo import DuckDuckGO


def test_search_expression(driver):
    '''
    :param driver: funtion present in conftest.py which return an instance of selenium web driver with yield
    :return: None
    '''
    search_expression = "python3"
    obj = DuckDuckGO(driver)
    obj.type_search_expression(search_expression)
    obj.click_search_button()
    assert search_expression in obj.get_current_url()
