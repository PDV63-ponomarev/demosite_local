import pytest
from selene import browser

from project import Config
from project import get_driver

def pytest_addoption(parser):
    parser.addoption(
        "--driver",
        action="store",
        default="chrome",
        help="Browser driver: chrome or firefox"
    )

@pytest.fixture(scope='session', autouse=True)
def browser_management(request):
    config = Config()

    driver_name = request.config.getoption("--driver")

    # driver = get_driver(config.driver_name)
    driver = get_driver(driver_name)

    browser.config.hold_browser_open = True
    browser.config.base_url = config.base_url
    browser.config.driver = driver
    browser.config.hold_driver_at_exit = config.hold_driver_at_exit
    browser.config.window_width = config.window_width
    browser.config.window_height = config.window_height
    browser.config.timeout = config.timeout

    yield browser

    # Закрываем браузер после теста
    if not config.hold_driver_at_exit:
        browser.quit()