todomvc-headless-firefox:
	pytest tests/test_todomvc.py --headless --browser=firefox -v

practice-form-local:
	pytest tests/test_demoqa_practice_form.py --noconftest  -v
