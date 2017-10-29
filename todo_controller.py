from todo_item import *
from todo_list import *


def create_task(task_name, task_description):
    task = ToDoItem(task_name, task_description)
    return task


def add_task_to_list(todo_tasks, task):
    todo_tasks.add_item(task)


def check_if_task_in_list(todo_tasks, task_name):
    for task in todo_tasks.todo_items:
        if task_name == task.name:
            return True
    raise ValueError


def delete_task_from_list(todo_tasks, task_name):
    for task in todo_tasks.todo_items:
        if task_name == task.name:
            todo_tasks.delete_item(task)
            break
    else:
        raise ValueError


def modify_task_name(todo_tasks, task_name, new_name):
    for task in todo_tasks.todo_items:
        if task_name == task.name:
            task.change_task_name(new_name)
            break


def modify_task_description(todo_tasks, task_name, new_description):
    for task in todo_tasks.todo_items:
        if task_name == task.name:
            task.change_task_description(new_description)
            break


def mark_task(todo_tasks, task_name):
    for task in todo_tasks.todo_items:
        if task_name == task.name:
            task.mark_item()
            break
    else:
        raise ValueError


def unmark_task(todo_tasks, task_name):
    for task in todo_tasks.todo_items:
        if task_name == task.name:
            task.unmark_item()
            break
    else:
        raise ValueError


def display_specific_task(todo_tasks, task_name):
    start_index = 1
    for index, task in enumerate(todo_tasks.todo_items, start_index):
        if task_name == task.name:
            print("ID:" + str(index) + " " + str(task))
            break
    else:
        raise ValueError


def initialize_tasks_list():
    todo_tasks = ToDoList()
    todo_tasks.load_items_from_file('saved_tasks.txt')
    return todo_tasks
