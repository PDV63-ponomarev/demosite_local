from selene import have, be, browser
import allure

@allure.title("Двойное нажатие")
def test_double_click():

    with allure.step('Открытие сайта'):
        browser.open('/buttons')

    with allure.step('Сообщения о клике нет'):
        browser.element('#doubleClickMessage').should(be.absent)

    with allure.step('Поиск кнопки'):
        double_click_btn = browser.element('#doubleClickBtn')
        double_click_btn.should(be.visible)
        double_click_btn.should(be.clickable)

    with allure.step('Двойное нажатие'):
        double_click_btn.double_click()

    with allure.step('Проверка появления текста'):
        browser.element('#doubleClickMessage').should(be.visible)

@allure.title("Нажатие правой кнопкой мыши")
def test_right_click():

    with allure.step('Открытие сайта'):
        browser.open('/buttons')

    with allure.step('Сообщения о клике нет'):
        browser.element('#rightClickMessage').should(be.absent)

    with allure.step('Поиск кнопки'):
        right_click_btn = browser.element('#rightClickBtn')
        right_click_btn.should(be.visible)
        right_click_btn.should(be.clickable)

    with allure.step('Правый клик'):
        right_click_btn.context_click()

    with allure.step('Проверка появления текста'):
        browser.element('#rightClickMessage').should(be.visible)

@allure.title("Нажатие на кнопку с динамическим ID")
def test_dynamic_click():

    with allure.step('Открытие сайта'):
        browser.open('/buttons')

    with allure.step('Сообщения о клике нет'):
        browser.element('#dynamicClickMessage').should(be.absent)

    with allure.step('Поиск кнопки'):
        button = (browser.all('.btn.btn-primary')
                  .element_by(have.exact_text('Click Me')))
        button.should(be.visible)
        button.should(be.clickable)

    with allure.step('Нажатие на кнопку'):
        button.click()

    with allure.step('Проверка появления текста'):
        browser.element('#dynamicClickMessage').should(be.visible)