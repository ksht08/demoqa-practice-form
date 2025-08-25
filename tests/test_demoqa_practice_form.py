from selene import browser, command, have, be
from selene.support.shared import config
import pytest

@pytest.fixture(scope='function', autouse=True)
def local_browser_setup():
    # config.hold_browser_open = True # do not close browser after test
    browser.config.base_url = "https://demoqa.com/automation-practice-form"
    browser.config.browser_name = "firefox"
    config.window_width = 1500
    config.window_height = 1024

    yield
    browser.quit()

FORM_DATA = {
    "first_name": "Margaret",
    "last_name": "Abercrombie",
    "full_name": "Margaret Abercrombie",
    "gender": "Female",
    "mobile": "1234567890",
    "date_of_birth": "08 Mar 1999",
    "email": "margaret.abercrombie@example.com"
    }

def test_practice_form():
    browser.open("/")
    h1 = browser.element("h1")
    h1.should(be.existing).should(be.visible).should(have.exact_text("Practice Form"))
    browser.element("#userName-wrapper #firstName").type(FORM_DATA["first_name"])
    browser.element("#userName-wrapper #lastName").type(FORM_DATA["last_name"])
    browser.element("#userEmail").type(FORM_DATA["email"])
    radio_female = browser.element('label[for="gender-radio-2"]')
    radio_female.click()
    browser.element("#gender-radio-2").should(have.attribute("value").value("Female")).should(be.selected)
    browser.element("#userNumber").should(be.blank)
    browser.element("#userNumber").should(have.attribute("placeholder").value("Mobile Number")).type(FORM_DATA["mobile"])
    browser.element("#userNumber").should(have.attribute("value").value(FORM_DATA["mobile"]))
    browser.element(".react-datepicker__input-container").perform(command.js.scroll_into_view)
    browser.element(".react-datepicker__input-container").click()
    browser.element(".react-datepicker-popper").should(be.visible)
    browser.element(".react-datepicker__month-select").click()
    browser.element('option[value="2"]').click()  # March
    browser.element(".react-datepicker__year-select").click()
    browser.element('option[value="1999"]').click()
    browser.element(".react-datepicker__day--008").should(have.no.css_class('--outside-month')).click()
    browser.element("#dateOfBirthInput").should(have.attribute("value").value(FORM_DATA["date_of_birth"])).should(be.visible)
    browser.element("#submit[type='submit']").perform(command.js.scroll_into_view)
    browser.element("#submit[type='submit']").click()
    browser.element(".modal-content").should(be.visible)
    browser.element(".modal-header").should(have.exact_text("Thanks for submitting the form"))
    table_rows = browser.all("table tbody tr")
    table_rows.element_by(have.text("Student Name")).element("td:nth-child(2)").should(have.exact_text(FORM_DATA["full_name"]))
    table_rows.element_by(have.text("Student Email")).element("td:nth-child(2)").should(have.exact_text(FORM_DATA["email"]))
    table_rows.element_by(have.text("Gender")).element("td:nth-child(2)").should(have.exact_text(FORM_DATA["gender"]))