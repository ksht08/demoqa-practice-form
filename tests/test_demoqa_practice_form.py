import pytest
from selene import browser
from selene.support.shared import config
from pages.demoqa_registration_form import RegistrationPage
from data.users import user

@pytest.fixture(scope='function', autouse=True)
def local_browser_setup():
    browser.config.base_url = "https://demoqa.com/automation-practice-form"
    browser.config.browser_name = "firefox"
    config.window_width = 1500
    config.window_height = 1024

    yield
    browser.quit()

def test_registration_form():
    registration_page = RegistrationPage()

    registration_page.open()
    registration_page.check_h1(user.h1)
    registration_page.fill_first_name(user.first_name)
    registration_page.fill_last_name(user.last_name)
    registration_page.fill_email(user.email)
    registration_page.select_gender(user.gender)
    registration_page.fill_mobile_number(user.mobile)
    registration_page.fill_date_of_birth(user.date_of_birth["year"],
                                           user.date_of_birth["month"],
                                           user.date_of_birth["day"],
                                           user.date_of_birth_short)
    registration_page.select_subjects(user.subjects)
    registration_page.select_hobbies(user.hobbies[1], user.hobbies[2])
    registration_page.upload_picture(user.picture_path)
    registration_page.submit_form()
    registration_page.assert_user_registration_info(user.full_name,
                                                    user.email,
                                                    user.gender,
                                                    user.mobile,
                                                    user.subjects,
                                                    user.hobbies[1],
                                                    user.hobbies[2],
                                                    user.picture)
    print(f"PICTURE PATH: {user.picture}")