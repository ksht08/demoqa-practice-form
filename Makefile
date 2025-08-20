headless-firefox:
	pytest $(TEST_FILE) --headless --browser=firefox -v
# make headless-firefox TEST_FILE=tests/test_todomvc.py

headless-chrome:
	pytest $(TEST_FILE) --headless --browser=chrome -v

chrome:
	pytest $(TEST_FILE) --browser=chrome -v

firefox:
	pytest $(TEST_FILE) --browser=firefox -v
	
chrome-noconftest:
	pytest $(TEST_FILE) --noconftest --browser=chrome -v

noconftest:
	pytest $(TEST_FILE) --noconftest -v
# make firefox-noconftest TEST_FILE=tests/test_demoqa_practice_form.py

todomvc-headless-firefox:
	pytest tests/test_todomvc.py --headless --browser=firefox -v

practice-form-local:
	pytest tests/test_demoqa_practice_form.py --noconftest  -v
