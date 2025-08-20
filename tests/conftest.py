import pytest
from selene import browser
from selene.support.shared import config
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser: chrome or firefox")
    parser.addoption("--headless", action="store_true",
                     help="Run in headless mode")


@pytest.fixture(scope='session', autouse=True)
def browser_management(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    drivers = {
        "chrome": (
            webdriver.ChromeOptions,
            "chrome",
            lambda options: (
                options.add_argument("--headless=new"),
                options.add_argument("--disable-gpu"),
            ),
        ),
        "firefox": (
            webdriver.FirefoxOptions,
            "firefox",
            lambda options: setattr(options, "headless", True),
        ),
    }

    if browser_name not in drivers:
        raise ValueError(f"Browser '{browser_name}' is not supported!")

    options_class, selene_browser_name, headless_setup = drivers[browser_name]
    options = options_class()

    if headless:
        headless_setup(options)

    # Selene config
    config.browser_name = selene_browser_name
    config.base_url = "https://todomvc.com/examples/emberjs/todomvc/dist/"
    config.window_width = 1280
    config.window_height = 1024
    config.driver_options = options
    config.timeout = 4.0

    browser.open("/")
    yield
    browser.quit()
