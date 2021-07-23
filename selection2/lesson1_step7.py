from selenium import webdriver
import time
import math


def calc(x):
    # 4. Посчитать математическую функцию от x (сама функция остаётся неизменной).
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    # 1. Открыть страницу по URL.
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 2. Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    x_element_treasure = browser.find_element_by_id("treasure")
    # 3. Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x_element = x_element_treasure.get_attribute("valuex")
    x = x_element
    y = calc(x)

    # 5. Ввести ответ в текстовое поле.
    input1 = browser.find_element_by_id("answer")
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
