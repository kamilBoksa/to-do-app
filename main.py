from todo_controller import *
import os
import datetime


def import_ui():
    ui = []
    with open('user_interface.txt') as ui_file:
        for line in ui_file:
            ui.append(line)
    ui.insert(1, get_current_date())
    return "".join(ui)


def get_current_date():
    now = datetime.datetime.now()
    return now.strftime("|Today's date: %d-%m-%Y|" + "\n")


def create_task_name():
    while True:
        task_name = input("Enter task name (max 20 chars): ")
        if len(task_name) > 20:
            print("Too long task name!")
            continue
        elif len(task_name) == 0:
            print("Task name cannot be empty!")
            continue
        return task_name


def create_task_description():
    while True:
        task_description = input("Enter task description (max 150 chars):")
        if len(task_description) > 150:
            print("Too long task description!")
            continue
        return task_description


def handle_user_choice(tasks_list):
    while True:
        try:
            os.system("clear")
            print(import_ui())
            choice = input("User choice: ")
            if choice == "1":
                task_name = create_task_name()
                task_description = create_task_description()
                task = create_task(task_name, task_description)
                add_task_to_list(tasks_list, task)
            elif choice == "2":
                    task_name = input("Enter name of task you want to edit: ")
                    if check_if_task_in_list(tasks_list, task_name):
                        decision = input("""
                                    [1] Edit name.
                                    [2] Edit description.
                                    : """)
                        if decision == "1":
                            while True:
                                new_name = input("Enter task new name: ")
                                if len(new_name) > 20:
                                    print("Too long task name!")
                                    continue
                                modify_task_name(tasks_list, task_name, new_name)
                                break
                        elif decision == "2":
                            while True:
                                new_description = input("Enter task new description: ")
                                if len(new_description) > 150:
                                    print("Too long task description!")
                                    continue
                                modify_task_description(tasks_list, task_name, new_description)
                                break
                        else:
                            print("Wrong  decision input!")
            elif choice == "3":
                task_name = input("Enter name of task you want to delete: ")
                delete_task_from_list(tasks_list, task_name)
            elif choice == "4":
                task_name = input("Enter name of task you want to mark: ")
                mark_task(tasks_list, task_name)
            elif choice == "5":
                task_name = input("Enter name of task you want to unmark: ")
                unmark_task(tasks_list, task_name)
            elif choice == "6":
                print(tasks_list)
            elif choice == "7":
                task_name = input("Enter name of task you want to display: ")
                display_specific_task(tasks_list, task_name)
            elif choice == "0":
                tasks_list.save_items_to_file('saved_tasks.txt')
                exit()
            else:
                print("Invalid input!")
        except ValueError:
            print("No task with that name found!")

        wait_time = input("Press any key to continue")


def main():
    tasks_list = initialize_tasks_list()
    handle_user_choice(tasks_list)


if __name__ == "__main__":
    main()
