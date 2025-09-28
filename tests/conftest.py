import pytest
import allure
import sys
import platform
from selene import browser
from selene.support.shared import config
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser: chrome or firefox")
    parser.addoption("--headless", action="store_true",
                     help="Run in headless mode")

# add browser/OS info to allure report
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    browser = item.config.getoption("--browser")
    headless = item.config.getoption("--headless")

    allure.dynamic.tag(browser) # browser name
    allure.dynamic.tag(f"headless={headless}") # headless = True/False
    allure.dynamic.tag(f"{platform.system()} {platform.release()}") # OS name + OS version
    allure.dynamic.tag(f"python={sys.version.split()[0]}") # python version

    allure.dynamic.epic(browser)
    allure.dynamic.feature(f"headless={headless}")
    allure.dynamic.story(f"{platform.system()} {platform.release()}")

    # for different test uid in allure reports
    allure.dynamic.parameter("browser", browser)
    allure.dynamic.parameter("headless", f"headless={headless}")

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
            lambda options: (
                options.add_argument("--headless"),
                options.add_argument("--disable-gpu"),
            ),
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
    config.base_url = "https://demoqa.com/automation-practice-form"
    config.window_width = 1500
    config.window_height = 1024
    config.driver_options = options
    config.timeout = 4.0

    browser.open("/")
    yield
    browser.quit()
