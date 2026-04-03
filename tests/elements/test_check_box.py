import allure
from selene import be, have, browser

def open_box():
    current_count = len(browser.all('.rc-tree-switcher_close'))
    while current_count > 0 and current_count != -1:
        for folder in browser.all('.rc-tree-switcher_close'):
            if folder.matching(be.visible):
                folder.click()
        current_count = len(browser.all('.rc-tree-switcher_close'))

@allure.title("Открытие всех папок")
def test_open_box():

    with allure.step('Открытие сайта'):
        browser.open('/checkbox')

    with allure.step('Раскрытие ветки'):
        open_box()

    with allure.step('Свернутых папок нет'):
        assert len(browser.all('.rc-tree-switcher_close')) == 0


@allure.title("Выбор всех чекбоксов")
def test_check_boxes():

    with allure.step('Открытие сайта'):
        browser.open('/checkbox')

    with allure.step('Раскрытие ветки'):
        open_box()

    with allure.step('Выбор общей папки'):
        browser.element('[aria-label="Select Home"]').click()

    with allure.step('Проверка выбора всех папок'):
        for element in browser.all('.rc-tree-checkbox'):
            element.should(have.css_class('rc-tree-checkbox-checked'))

    with allure.step('Выбранные элементы присутствуют в поле результат'):
        selected_checkboxes = browser.all('.rc-tree-checkbox-checked')
        selected_texts = []

        for checkbox in selected_checkboxes:
            text_element = checkbox.element('./..//span[contains(@class, "rc-tree-title")]')
            text = text_element.locate().text
            if text == 'Word File.doc':
                selected_texts.append('wordFile')
            elif text == 'Excel File.doc':
                selected_texts.append('excelFile')
            else:
                selected_texts.append(text.lower())

        expected_text = ' '.join(selected_texts)

        for word in browser.all('.text-success'):
            word = word.locate().text
            assert word in expected_text