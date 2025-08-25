from selene import browser, command, have, be, query
from selene.support.shared import browser, config
from selenium import webdriver
import time
import os, requests
import pytest

# 'tests\' - enter the 'tests' folder
# '..' - go up one level (to the root of the project)
# 'TMP' - enter the 'TMP' folder
TMP_DIR = os.path.join(os.path.dirname(__file__), '..', 'TMP')
README_FILE = os.path.join(TMP_DIR, "README.rst")

@pytest.fixture(scope='function', autouse=True)
def local_browser_setup():
    # options = webdriver.FirefoxOptions()
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": TMP_DIR, # sets the default download directory
        "download.prompt_for_download": False, # disables the download prompt
        "download.directory_upgrade": True, # ensures the directory is created if it does not exist
        "safebrowsing.enabled": True, # enables safe browsing features
        "plugins.always_open_pdf_externally": True, # enables opening PDF files externally
        "download.extensions_to_open": "applications/octet-stream,text/plain,text/x-rst", # auto open specified file types
        "profile.default_content_settings.popups": 0, # disables popups
        "profile.content_settings.exceptions.automatic_downloads.*.setting": 1, # allows automatic downloads
    }
    options.add_experimental_option("prefs", prefs)
    browser.config.driver_options = options
    browser.config.base_url = "https://github.com/pytest-dev/pytest/blob/main/README.rst"
    browser.config.browser_name = "chrome"
    config.window_width = 1500
    config.window_height = 1024
    browser.open("/")
    yield
    browser.quit()

@pytest.fixture(scope='session', autouse=True)
def cleanup_after_all_tests():
    yield
    # delete all files in TMP folder
    for file in os.listdir(TMP_DIR):
        file_path = os.path.join(TMP_DIR, file)
        if os.path.isfile(file_path):
            os.remove(file_path)

def test_download_readme_file():
    # readme_raw_button = browser.element("[data-testid='raw-button']").locate()
    # readme_raw_url = readme_raw_button.get_attribute("href")
    readme_raw_url = browser.element("[data-testid='raw-button']").get(query.attribute("href"))
    req = requests.get(readme_raw_url) # request to README.rst URL
    readme_filepath = os.path.join(TMP_DIR, "README.rst") # full path to README.rst
    with open(readme_filepath, "wb") as downloaded_file: # open file in binary mode for writing
        downloaded_file.write(req.content) # writes all bytes received from the HTTP response to README.rst
    assert os.path.exists(readme_filepath) # checks that README.rst actually exists at the specified path
    time.sleep(3) # wait (for debugging purposes)

def test_read_readme_file():
    readme_filepath = os.path.join(TMP_DIR, "README.rst") # full path to README.rst
    with open(readme_filepath) as f:
        file_content = f.read()
        assert "https://github.com/pytest-dev/pytest/blob/main/LICENSE" in file_content

def test_create_file():
    file_path = os.path.join(TMP_DIR, "new file.txt")
    with open(file_path, "w") as f:
        f.write("hello!\nHow are you?")
    with open(file_path) as f:
        file_content = f.read()
        assert "How are you" in file_content
