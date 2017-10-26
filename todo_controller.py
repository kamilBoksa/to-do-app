from todo_item import *
from todo_list import *


def create_task():
    creating_task = True
    while creating_task:
        task_name = input("Enter task name (max 20 chars): ")
        if len(task_name) > 20:
            print("Too long task name!")
            continue
        break
    while creating_task:
        task_description = input("Enter task description (max 150 chars):")
        if len(task_description) > 150:
            print("Too long task description!")
            continue
        task = ToDoItem(task_name, task_description)
        return task


def add_task_to_list(todo_items, task):
    todo_items.add_item(task)


def delete_task_from_list(todo_items):
    try:
        item_name = input("Enter name of task you want to delete: ")
        if item_name in task_list:
            task_list.delete_item(item_name)
    except ValueError:
        print("No task with that name found!")


def handle_ui_choice():
    todo_items = ToDoList()

    while True:
        choice = input("User choice: ")
        if choice == "1":
            add_task_to_list(todo_items, create_task())
        if choice == "2":
            pass  # modify task
        if choice == "3":
            delete_task_from_list(todo_items)
        elif choice == "4":
            pass  # mark task
        elif choice == "5":
            pass  # display tasks
        elif choice == "6":
            pass  # display specific task
        elif choice == "0":
            exit()
        else:
            print("Invalid input!")
