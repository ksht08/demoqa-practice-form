headless-firefox:
	pytest $(TEST_FILE) --headless --browser=firefox -v
# make headless-firefox TEST_FILE=tests/<test_file_name>

headless-chrome:
	pytest $(TEST_FILE) --headless --browser=chrome -v

chrome:
	pytest $(TEST_FILE) --browser=chrome -v

firefox:
	pytest $(TEST_FILE) --browser=firefox -v
	
noconftest:
	pytest $(TEST_FILE) --noconftest -v
# make firefox-noconftest TEST_FILE=tests/<test_file_name>
