from todo_item import *


class ToDoList:

    def __init__(self):
        self.todo_items = []

    def add_item(self, item):
        self.todo_items.append(item)

    def delete_item(self, item_name):
        try:
            self.todo_items.remove(item_name)
        except ValueError:
            pass

    def __str__(self):
        index_start = 1
        display_list = []
        for index, item in enumerate(self.todo_items, index_start):
            display_list.append(str(index)+". "+str(item))
        return "".join(display_list)
