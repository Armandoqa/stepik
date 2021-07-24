from selenium import webdriver
import unittest
import time


class TestUnittest(unittest.TestCase):
    def test_first(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_xpath("//input[@class='form-control first']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//input[@class='form-control third']")
        input3.send_keys("Ivan.Petrov@gmail.com")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_second(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_xpath("//input[@class='form-control first']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//input[@class='form-control third']")
        input3.send_keys("Ivan.Petrov@gmail.com")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
