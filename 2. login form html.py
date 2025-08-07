from selene import browser, have, be
from selene.support.shared import config
import os

config.hold_browser_open = True # do not close browser after test
url = "file://" + os.path.abspath("login_form.html") # open local HTML file
get_parameter_login = "?login=true"  # query parameter to check in URL
browser.config.browser_name = "firefox"

browser.open(url)
header = browser.element("h1")
header.should(be.existing).should(be.visible).should(have.exact_text("Login Form")) # find exact text "Login Form"
header.should(be.existing).should(be.visible).should(have.text("Login")) # find text that contains "Login"

phone = browser.element("#phone")
(phone.should(be.visible).should(have.no.attribute("required"))
      .should(have.attribute("placeholder", "Optional"))) # phone input should not be required

username_input = browser.element("#username")
username_input.should(be.visible).should(have.attribute("required")).type("test user")

password_input = browser.element("#password")
password_input.should(be.visible).should(have.attribute("required")).type("password")

success_msg = browser.element("#successMessage")
success_msg.should(be.not_.visible)  # initially not visible

login_button = browser.element('button[type="submit"]')
login_button.should(be.visible).should(have.attribute("value", "Log In")).click()
(success_msg.should(be.visible)
            .should(have.text("Log In successful"))
            .should(have.css_property("color", "rgb(0, 128, 0)"))) # should be visible after successful login and green color

browser.should(have.url_containing(get_parameter_login)) # check URL contains query parameter

username_input.should(be.blank)  # input should be cleared after login
password_input.should(be.blank)  # input should be cleared after login
