from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    # 1. Открыть страницу по URL.
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 2. Нажать на кнопку
    button1 = browser.find_element_by_css_selector(".trollface")
    button1.click()

    # 3. Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # 4. На новой странице решить капчу для роботов, чтобы получить число с ответом
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button2 = browser.find_element_by_css_selector(".btn")
    button2.click()

    print(browser.switch_to.alert.text)

finally:
    browser.quit()
