from selene import browser, have, be
from selene.support.shared import config

config.hold_browser_open = True # do not close browser after test
browser.config.base_url = "https://google.com"
browser.config.browser_name = "firefox"

browser.open("/")
browser.element('[id="L2AGLb"]').should(be.visible).should(have.text("Hyväksy kaikki")).click()
browser.element("[name='q']").should(be.visible).type("Selene Python").press_enter()
browser.element("[id='search']").should(have.text("Selene is a concise and powerful library"))