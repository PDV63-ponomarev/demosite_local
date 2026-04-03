import time
from selene import be, have, browser
import allure

@allure.title("Активация кнопки после 5 секунд")
def un_test_enable_button():

    with allure.step('Открытие сайта'):
        browser.open('/dynamic-properties')

    with allure.step('Поиск кнопки'):
        enable_button = browser.element('#enableAfter')
        enable_button.should(be.visible)

    with allure.step('Кнопка неактивна'):
        enable_button.should(be.disabled)

    with allure.step('Ожидание 5 сек'):
        time.sleep(5)

    with allure.step('Проверка активации цнопки'):
        enable_button.should(be.clickable)

@allure.title("Смена цвета кнопки после 5 секунд")
def un_test_change_button():

    with allure.step('Открытие сайта'):
        browser.open('/dynamic-properties')

    with allure.step('Поиск кнопки'):
        change_button = browser.element('#colorChange')
        change_button.should(be.visible)

    with allure.step('Кнопка активна'):
        change_button.should(be.clickable)

    with allure.step('Кнопка не имеет спец цвета'):
        change_button.should(have.no.css_class('text-danger'))

    with allure.step('Ожидание 5 сек'):
        time.sleep(5)

    with allure.step('Кнопка имеет спец цвет'):
        change_button.should(have.css_class('text-danger'))

@allure.title("Видимость кнопки после 5 секунд")
def un_test_visible_button():

    with allure.step('Открытие сайта'):
        browser.open('/dynamic-properties')

    with allure.step('Кнопка отсутствует в DOM'):
        visible_button = browser.element('#visibleAfter')
        visible_button.should(be.not_.present)

    with allure.step('Ожидание 5 сек'):
        time.sleep(5)

    with allure.step('Кнопка появилась'):
        visible_button.should(be.visible)
        visible_button.should(be.clickable)

@allure.title("Комплексная проверка всех кнопок через 5 секунд")
def test_complite_button():

    with allure.step('Открытие сайта'):
        browser.open('/dynamic-properties')

    with allure.step('Поиск неактивной кнопки'):
        enable_button = browser.element('#enableAfter')
        enable_button.should(be.visible)
        enable_button.should(be.disabled)

    with allure.step('Поиск кнопки со сменой цвета'):
        change_button = browser.element('#colorChange')
        change_button.should(be.visible)
        change_button.should(be.clickable)
        change_button.should(have.no.css_class('text-danger'))

    with allure.step('Поиск отсутствующей кнопки'):
        visible_button = browser.element('#visibleAfter')
        visible_button.should(be.not_.present)

    with allure.step('Ожидание 5 сек'):
        time.sleep(5)

    with allure.step('Проверка активации цнопки'):
      enable_button.should(be.clickable)

    with allure.step('Кнопка имеет спец цвет'):
        change_button.should(have.css_class('text-danger'))

    with allure.step('Кнопка появилась'):
        visible_button.should(be.visible)
        visible_button.should(be.clickable)