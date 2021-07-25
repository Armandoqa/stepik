# pytest -s -v /Users/armandoz/Documents/PyCharm/Stepik/selection3/test_lesson6_step3_1.py
import pytest
import time
import math
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('links', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_find_hidden_text(browser, links):
    link = f"https://stepik.org/lesson/{links}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)

    textarea = browser.find_element_by_css_selector("textarea")
    textarea.send_keys(str(math.log(int(time.time()))))

    button = browser.find_element_by_class_name("submit-submission")
    button.click()

    answer = browser.find_element_by_class_name("smart-hints__hint").text

    assert 'Correct!' == answer
