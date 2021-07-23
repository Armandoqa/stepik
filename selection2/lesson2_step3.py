from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try:
    # 1. Открыть страницу по URL.
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element_by_id("num1")
    x = number1.text
    number2 = browser.find_element_by_id("num2")
    y = number2.text
    # 2. Посчитать сумму заданных чисел
    s = (int(x)+int(y))

    # 3. Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(s))

    # 4. Нажать кнопку "Submit"
    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
