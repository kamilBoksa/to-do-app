from todo_item import *
from todo_list import *


def create_task(task_name, task_description):
    task = ToDoItem(task_name, task_description)
    return task


def add_task_to_list(todo_items, task):
    todo_items.add_item(task)


def check_if_task_in_list(todo_items, task_name):
    for task in todo_items.todo_items:
        if task_name == task.name:
            return True
    raise ValueError


def delete_task_from_list(todo_items, task_name):
    for task in todo_items.todo_items:
        if task_name == task.name:
            todo_items.delete_item(task)
            break
    else:
        raise ValueError


def modify_task_name(todo_items, task_name, new_name):
    for task in todo_items.todo_items:
        if task_name == task.name:
            task.change_task_name(new_name)
            break


def modify_task_description(todo_items, task_name, new_description):
    for task in todo_items.todo_items:
        if task_name == task.name:
            task.change_task_description(new_description)
            break


def mark_task(todo_items, task_name):
    for task in todo_items.todo_items:
        if task_name == task.name:
            task.mark_item()
            break
    else:
        raise ValueError


def unmark_task(todo_items, task_name):
    for task in todo_items.todo_items:
        if task_name == task.name:
            task.unmark_item()
            break
    else:
        raise ValueError


def display_specific_task(todo_items, task_name):
    for index, task in enumerate(todo_items.todo_items, 1):
        if task_name == task.name:
            print("ID:" + str(index) + " " + str(task))
            break
    else:
        raise ValueError


def initialize_tasks_list():
    todo_items = ToDoList()
    todo_items.load_items_from_file('saved_tasks.txt')
    return todo_items
