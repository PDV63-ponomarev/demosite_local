from selene import have, browser
import allure

full_name = 'Иванов Иван'
email = 'ivanov@gmail.com'
address = 'Some adress'

@allure.title("Заполнение текстовой формы")
def test_simple_form():
    with allure.step('Открытие сайта'):
        browser.open('/text-box')
        browser.driver.execute_script("document.body.style.zoom='75%'")

    with allure.step('Заполнение полей'):
        browser.element('#userName').type(full_name)
        browser.element('#userEmail').type(email)
        browser.element('#currentAddress').type(address)
        browser.element('#submit').click()

    with allure.step('Проверка заполненности'):
        output = browser.element('#output')
        output.should(have.text(f'Name:{full_name}'))
        output.should(have.text(f'Email:{email}'))
        output.should(have.text(f'Current Address :{address}'))