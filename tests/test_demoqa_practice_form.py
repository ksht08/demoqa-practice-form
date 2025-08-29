import os, pytest
from selene import browser, command, have, be
from selene.support.shared import config

RESOURCES_DIR = os.path.join(os.path.dirname(__file__), '..', 'resources')
PICTURE = "avatar.jpg"
PICTURE_PATH = os.path.join(RESOURCES_DIR, PICTURE)

FORM_DATA = {
    "first_name": "Margaret",
    "last_name": "Abercrombie",
    "full_name": "Margaret Abercrombie",
    "gender": "Female",
    "mobile": "1234567890",
    "picture": PICTURE,
    "hobbies": ["Sports", "Reading", "Music"],
    "subjects": "Social Studies",
    "date_of_birth": "08 Mar 1999",
    "email": "margaret.abercrombie@example.com"
    }

@pytest.fixture(scope='function', autouse=True)
def local_browser_setup():
    browser.config.base_url = "https://demoqa.com/automation-practice-form"
    browser.config.browser_name = "firefox"
    config.window_width = 1500
    config.window_height = 1024

    yield
    browser.quit()

def test_practice_form():
    browser.open("/")

    # check h1
    h1 = browser.element("h1")
    h1.should(be.existing).should(be.visible).should(have.exact_text("Practice Form"))

    # fill first name
    browser.element("#userName-wrapper #firstName").type(FORM_DATA["first_name"])

    # fill last name
    browser.element("#userName-wrapper #lastName").type(FORM_DATA["last_name"])

    # fill email
    browser.element("#userEmail").type(FORM_DATA["email"])

    # check gender
    radio_female = browser.element('label[for="gender-radio-2"]')
    radio_female.click()
    browser.element("#gender-radio-2").should(have.attribute("value").value("Female")).should(be.selected)

    # fill mobile number
    browser.element("#userNumber").should(be.blank)
    browser.element("#userNumber").should(have.attribute("placeholder").value("Mobile Number")).type(FORM_DATA["mobile"])
    browser.element("#userNumber").should(have.attribute("value").value(FORM_DATA["mobile"]))

    # fill date of birth
    browser.element(".react-datepicker__input-container").perform(command.js.scroll_into_view)
    browser.element(".react-datepicker__input-container").click()
    browser.element(".react-datepicker-popper").should(be.visible)
    browser.element(".react-datepicker__month-select").click()
    browser.element('option[value="2"]').click()  # March
    browser.element(".react-datepicker__year-select").click()
    browser.element('option[value="1999"]').click()
    browser.element(".react-datepicker__day--008").should(have.no.css_class('--outside-month')).click()
    browser.element("#dateOfBirthInput").should(have.attribute("value").value(FORM_DATA["date_of_birth"])).should(be.visible)

    # fill subject
    browser.element("#subjectsInput").type("social")
    browser.element(".subjects-auto-complete__menu-list").should(be.visible).should(have.exact_text("Social Studies")).click()

    # check hobbies
    checkbox_hobbie = browser.all("#hobbiesWrapper .custom-checkbox")
    checkbox_hobbie.element_by(have.text("Reading")).click()
    checkbox_hobbie.element_by(have.text("Music")).click()

    # upload picture
    browser.element("#uploadPicture").set_value(PICTURE_PATH)

    # click Submit button
    browser.element("#submit[type='submit']").perform(command.js.scroll_into_view)
    browser.element("#submit[type='submit']").click()

    # check modal
    browser.element(".modal-content").should(be.visible)
    browser.element(".modal-header").should(have.exact_text("Thanks for submitting the form"))
    table_rows = browser.all("table tbody tr")
    table_rows.element_by(have.text("Student Name")).element("td:nth-child(2)").should(have.exact_text(FORM_DATA["full_name"]))
    table_rows.element_by(have.text("Student Email")).element("td:nth-child(2)").should(have.exact_text(FORM_DATA["email"]))
    table_rows.element_by(have.text("Gender")).element("td:nth-child(2)").should(have.exact_text(FORM_DATA["gender"]))
    table_rows.element_by(have.text("Mobile")).element("td:nth-child(2)").should(have.exact_text(FORM_DATA["mobile"]))
    table_rows.element_by(have.text("Subjects")).element("td:nth-child(2)").should(have.exact_text(FORM_DATA["subjects"]))
    table_rows.element_by(have.text("Hobbies")).element("td:nth-child(2)").should(
    have.exact_text(f"{FORM_DATA['hobbies'][1]}, {FORM_DATA['hobbies'][2]}"))
    table_rows.element_by(have.text("Picture")).element("td:nth-child(2)").should(have.exact_text(FORM_DATA["picture"]))