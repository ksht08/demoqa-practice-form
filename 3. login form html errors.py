from selene import browser, have, be
from selene.support.shared import config
import os

config.hold_browser_open = True # do not close browser after test
url = "file://" + os.path.abspath("login_form.html") # open local HTML file
browser.config.browser_name = "firefox"

browser.open(url)
username_input = browser.element("#username")
username_input.type("us")

password_input = browser.element("#password")
password_input.type("pw")

username_error = browser.element("#usernameError")
username_error.should(be.not_.visible)  # initially not visible

password_error = browser.element("#passwordError")
password_error.should(be.not_.visible)  # initially not visible

login_button = browser.element('[type="submit"]')
login_button.click()

success_msg = browser.element("#successMessage")
success_msg.should(be.not_.visible)  # should not be visible before validation

#check error messages after button click
(username_error.should(be.visible)
               .should(have.text("Username must be between 3 and 12 characters"))
               .should(have.css_property("color", "rgb(255, 0, 0)")))  # should be red color
            
(password_error.should(be.visible)
               .should(have.text("Password must be between 3 and 12 characters"))
               .should(have.css_property("color", "rgb(255, 0, 0)")))  # should be red color