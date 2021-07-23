from selenium import webdriver
import time
import math


def calc(x):
    # 3. Посчитать математическую функцию от x.
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    # 1. Открыть страницу по URL.
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 2. Считать значение для переменной x.
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # 4. Проскроллить страницу вниз.
    input1 = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    # 5. Ввести ответ в текстовое поле.
    input1.send_keys(y)

    # 6. Отметить checkbox "I'm the robot".
    checkbox1 = browser.find_element_by_id("robotCheckbox")
    checkbox1.click()

    # 7. Выбрать radiobutton "Robots rule!".
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    # 8. Нажать на кнопку Submit.
    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
