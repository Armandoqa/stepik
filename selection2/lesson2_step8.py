import os
import time
from selenium import webdriver


try:
    # 1. Открыть страницу по URL.
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 2. Заполнить текстовые поля: имя, фамилия, email
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Ivan.Petrov@gmail.com")

    # 3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    # получаем путь к директории текущего исполняемого скрипта lesson2_step8.py
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # имя файла, который будем загружать на сайт
    file_name = "lesson2_step8.txt"
    # получаем путь к file_example.txt
    file_path = os.path.join(current_dir, file_name)
    # отправляем файл
    input4 = browser.find_element_by_name("file")
    input4.send_keys(file_path)

    # 4. Нажать кнопку "Submit"
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
