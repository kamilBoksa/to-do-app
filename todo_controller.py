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


def handle_ui_choice():
    while True:
        choice = input("User choice: ")
        if choice == "1":
            pass
        if choice == "2":
            pass
        if choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "0":
            exit()
        else:
            print("Invalid input!")
