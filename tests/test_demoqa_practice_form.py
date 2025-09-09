import allure
from selene import browser
from pages.demoqa_registration_form import RegistrationPage
from data.users import user

allure.feature("DemoQA Practice Form")
allure.story("User Registration Form Submission")
@allure.title("Test User Registration Form")
@allure.description("""
This test fills out and submits the user registration form on DemoQA and verifies the submission.
""")
def test_registration_form():
    registration_page = RegistrationPage()

    with allure.step("Open registration page"):
        registration_page.open()

    with allure.step("Check h1 header"):
        registration_page.check_h1(user.h1)

    with allure.step("Fill out and submit the form"):
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
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="Filled Form Screenshot",
            attachment_type=allure.attachment_type.PNG
            )
        
    with allure.step("Submit the form"):
        registration_page.submit_form()

    with allure.step("Check submission results"):
        registration_page.assert_user_registration_info(
            user.full_name,
            user.email,
            user.gender,
            user.mobile,
            user.subjects,
            user.hobbies[1],
            user.hobbies[2],
            user.picture
        )
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="Modal Form with Filled Data Screenshot",
            attachment_type=allure.attachment_type.PNG
            )