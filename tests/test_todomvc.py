from selene import browser, command, have, be
import time
import pytest
# from selene.support.shared import config

@pytest.mark.ui
def test_open_todo_page():
    browser.should(have.title("TodoMVC"))

@pytest.mark.ui
def test_h1():
    h1 = browser.element("h1")
    h1.should(be.visible.and_(have.exact_text("todos")))
    # or
    h1.should(be.visible).should(have.exact_text("todos"))

@pytest.mark.ui
def test_todo_input():
    todo_input = browser.element(".new-todo")
    todo_input.should(be.visible.and_(be.blank))
    todo_input.should(have.attribute("placeholder").value("What needs to be done?"))

@pytest.mark.ui
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

@pytest.mark.ui
def test_complete_task():
    todo_toggle =  browser.all(".todo-list input.toggle")
    browser.element(".clear-completed").should(be.not_.existing)  # initially not visible
    count_toggle = len(todo_toggle)
    browser.element(".todo-count").should(have.text(f"{count_toggle} items left"))
    todo_toggle[1].click()  # check "task 2" checkbox
    browser.all(".todo-list li").element_by(have.exact_text("task 3")).element(".toggle").click() # check "task 3" checkbox
    completed_task_count = len(browser.all(".todo-list li").by(have.css_class("completed")))

    browser.element(".clear-completed").should(be.existing).should(be.visible)  # should be visible after completing a task
    browser.all("li").element_by(have.exact_text("task 2")).should(have.css_class("completed"))
    browser.element(".todo-count").should(have.text(f"{count_toggle - completed_task_count} items left"))
    todo_label = browser.all(".todo-list li .view label")
    todo_label[0].double_click() # double click on "task 1" to edit it
    browser.element(".todo-list li.editing .edit").click() # focus on the edit input
    edit_input = browser.element(".todo-list li.editing .edit")
    edit_input.perform(command.js.set_value("")).type("NEW name for 'TASK 1'").press_enter()
    

    time.sleep(3) # wait 3 seconds (for debugging purposes)