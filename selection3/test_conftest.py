# pytest -s -v --browser_name=chrome /Users/armandoz/Documents/PyCharm/Stepik/selection3/test_conftest.py
# pytest -s -v --browser_name=safari /Users/armandoz/Documents/PyCharm/Stepik/selection3/test_conftest.py
link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
