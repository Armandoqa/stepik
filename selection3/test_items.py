# pytest --language=es /Users/armandoz/Documents/PyCharm/Stepik/selection3/test_items.py
import time
from selenium.webdriver.common.by import By


def test_find_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(5)
    time.sleep(1)
    button = browser.find_element(By.XPATH, '//button[text()="Añadir al carrito"]').text
    assert 'Añadir al carrito' == button, "Error, different localization!"

    #assert browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket"), "Button 'basket' absent"


"""
import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_items(browser):
    browser.get(link) 
    time.sleep(5)  
    value = browser.find_element(By.NAME, "language").get_attribute("value")  
    if value == "ru":
        assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").text == "Добавить в корзину"
    elif value == "es":
        assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").text == "Añadir al carrito"     
    elif value == "fr":
        assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").text == "Ajouter au panier"  
    elif value == "de":
        assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket").text == "In Warenkorb legen"
    time.sleep(5)     
    browser.close()
"""