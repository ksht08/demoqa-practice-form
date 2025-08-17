from selene import browser, command, have, be
import time
# from selene.support.shared import config

def test_open_todo_page():
    browser.should(have.title("TodoMVC"))

def test_h1():
    h1 = browser.element("h1")
    h1.should(be.visible.and_(have.exact_text("todos")))
    # or
    h1.should(be.visible).should(have.exact_text("todos"))

def test_todo_input():
    todo_input = browser.element(".new-todo")
    todo_input.should(be.visible.and_(be.blank))
    todo_input.should(have.attribute("placeholder").value("What needs to be done?"))

def test_add_tasks():
    todo_input = browser.element(".new-todo")

    tasks_list = ["task 1", "task 2", "task 3"]
    for task_name in tasks_list:
        todo_input.type(task_name).press_enter()

    browser.all(".view label").should(have.exact_texts(*tasks_list))
    browser.all(".view label").by(have.text("task 3")).by(be.visible)

    todo_input.with_(type_by_js=True).type("this 111 is 2222 long 333333 title 4444444 for TASK 4").press_enter() # using JavaScript to type instantly
    # or
    todo_input.perform(command.js.type("this 555555 is 5555 long 5555555555 title 5555 for TASK 5")).press_enter()
    browser.all(".view label").should(have.size(5))
    todo_list = browser.all(".todo-list li .view label")
    # todo_list.with_(timeout=1).should(have.size(5)) # wait 1 second (for debugging purposes)
    for todo_task in todo_list:
        todo_task.should(be.visible)

def test_complete_task():
    todo_toggle= browser.all(".todo-list input.toggle")
    todo_toggle[1].click()  # click on "task 2" to complete it
    browser.all("li").element_by(have.exact_text("task 2")).should(have.css_class("completed"))
    count_toggle = len(todo_toggle)

    time.sleep(5) # wait 5 seconds (for debugging purposes)