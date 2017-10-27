from todo_item import *


class ToDoList:

    def __init__(self):
        self.todo_items = []

    def add_item(self, item):
        self.todo_items.append(item)

    def delete_item(self, item):
        self.todo_items.remove(item)

    @staticmethod
    def create_table_heading():
        heading = []
        max_name_len = 20
        additional_signs = 9  # used for adding more # ' ' or -

        title_border = "#" * (max_name_len + additional_signs)
        title_mid = "#" + " " * additional_signs + "TODO LIST" + " " * additional_signs + "#"
        columns_bottom = "-" * (max_name_len + additional_signs)
        additional_signs = 11
        columns_names = "| ID |    TASK NAME" + " " * additional_signs
        heading_elements = [title_border, title_mid, title_border, columns_names, columns_bottom]

        for element in heading_elements:
            heading.append(element + "\n")
        return heading

    def __str__(self):
        index_start = 1
        display_list = []
        max_name_len = 20
        additional_signs = 9

        heading = self.create_table_heading()
        underline = "-" * (max_name_len + additional_signs)
        display_list.append("".join(heading))

        for index, item in enumerate(self.todo_items, index_start):
            display_list.append("|  " + str(index) + " | " + str(item.name) + "\n")
            display_list.append(underline + "\n")
        return "".join(display_list)
