from selene import browser, have, be, command

class RegistrationPage():
    def __init__(self):
        self.browser = browser

    def open(self):
        browser.open("/")
        return self

    def check_h1(self, value):
        """
        Check h1 header
        """
        h1 = browser.element("h1")
        h1.should(be.existing).should(be.visible).should(have.exact_text(value))

    def fill_first_name(self, value):
        """
        Fill first name
        """
        browser.element("#userName-wrapper #firstName").type(value)

    def fill_last_name(self, value):
        """
        Fill last name
        """
        browser.element("#userName-wrapper #lastName").type(value)

    def fill_email(self, value):
        """
        Fill email
        """
        browser.element("#userEmail").type(value)
    
    def select_gender(self, value):
        """
        Select gender
        """
        radio_female = browser.element('label[for="gender-radio-2"]')
        radio_female.click()
        browser.element("#gender-radio-2").should(have.attribute("value").value(value)).should(be.selected)

    def fill_mobile_number(self, value):
        """
        Fill mobile number
        """
        browser.element("#userNumber").should(have.attribute("placeholder").value("Mobile Number")).type(value)
        browser.element("#userNumber").should(have.attribute("value").value(value))

    def fill_date_of_birth(self, year, month, day, date_short):
        """
        Select date of birth
        """
        browser.element(".react-datepicker__input-container").perform(command.js.scroll_into_view)
        browser.element(".react-datepicker__input-container").click()
        browser.element(".react-datepicker-popper").should(be.visible)
        browser.element(".react-datepicker__month-select").type(month) # month = March
        browser.element(".react-datepicker__year-select").type(year) # year = 1999
        browser.element(f".react-datepicker__day--0{day}").should(have.no.css_class('--outside-month')).click() # day = 08
        browser.element("#dateOfBirthInput").should(have.attribute("value").value(date_short)).should(be.visible)

    def select_subjects(self, value):
        """
        Select subjects
        """
        browser.element("#subjectsInput").type("social")
        browser.element(".subjects-auto-complete__menu-list").should(be.visible).should(have.exact_text(value)).click()

    def select_hobbies(self, *values):
        """
        Select hobbies
        """
        checkbox_hobbie = browser.all("#hobbiesWrapper .custom-checkbox")
        for hobbie_value in values:
            checkbox_hobbie.element_by(have.text(hobbie_value)).click()

    def upload_picture(self, value):
        """
        Upload picture
        """
        browser.element("#uploadPicture").set_value(value)

    def submit_form(self):
        """
        Submit the form
        """
        browser.element("#submit[type='submit']").perform(command.js.scroll_into_view)
        browser.element("#submit[type='submit']").click()

    def assert_user_registration_info(self, full_name, email, gender, mobile, subjects, hobbie1, hobbie2, picture):
        """
        Verify user registration info
        """
        browser.element(".modal-content").should(be.visible)
        browser.element(".modal-header").should(have.exact_text("Thanks for submitting the form"))
        table_rows = browser.all("table tbody tr")
        table_rows.element_by(have.text("Student Name")).element("td:nth-child(2)").should(have.exact_text(full_name))
        table_rows.element_by(have.text("Student Email")).element("td:nth-child(2)").should(have.exact_text(email))
        table_rows.element_by(have.text("Gender")).element("td:nth-child(2)").should(have.exact_text(gender))
        table_rows.element_by(have.text("Mobile")).element("td:nth-child(2)").should(have.exact_text(mobile))
        table_rows.element_by(have.text("Subjects")).element("td:nth-child(2)").should(have.exact_text(subjects))
        table_rows.element_by(have.text("Hobbies")).element("td:nth-child(2)").should(
        have.exact_text(f"{hobbie1}, {hobbie2}"))
        table_rows.element_by(have.text("Picture")).element("td:nth-child(2)").should(have.exact_text(picture))