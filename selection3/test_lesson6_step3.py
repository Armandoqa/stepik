# pytest -s -v /Users/armandoz/Documents/PyCharm/Stepik/selection3/test_lesson6_step3.py
import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('links', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, links):
        link = f"https://stepik.org/lesson/{links}/step/1"
        browser.get(link)
        browser.implicitly_wait(10)

        textarea = browser.find_element_by_css_selector("textarea")
        textarea.send_keys(str(math.log(int(time.time()))))

        button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        button.click()

        answer = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )
        assert "Correct!" == answer.text, "NOT CORRECT!"
