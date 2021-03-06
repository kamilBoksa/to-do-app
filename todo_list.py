from todo_item import *


class ToDoList:

    def __init__(self):
        self.todo_items = []

    def add_item(self, item):
        self.todo_items.append(item)

    def delete_item(self, item):
        self.todo_items.remove(item)

    def save_items_to_file(self, file_name):
        with open(file_name, 'w') as export_file:
            for line in self.todo_items:
                export_file.write(str(line)+'\n')

    def load_items_from_file(self, file_name):
        done_status = '[x]'
        try:
            with open(file_name, 'r') as import_file:
                for line in import_file:
                    line = line.strip('\n')
                    separator = "-"
                    item_deatails = line.split(separator)
                    status_index = 2
                    name_index = 0
                    description_index = 1
                    if done_status in item_deatails[status_index]:
                        item = ToDoItem(item_deatails[name_index].strip(),
                                        item_deatails[description_index].strip(), True)
                        item.mark_item()
                    else:
                        item = ToDoItem(item_deatails[name_index].strip(), item_deatails[description_index].strip())
                    self.todo_items.append(item)
        except IndexError:
            pass

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
        """
        Returns tasks list formatted in table form, with heading and column names
        """

        index_start = 1
        display_list = []
        max_name_len = 20
        additional_signs = 9

        heading = self.create_table_heading()
        underline = "-" * (max_name_len + additional_signs)
        display_list.append("".join(heading))

        for index, item in enumerate(self.todo_items, index_start):
            display_list.append("|  " + str(index) + " | " + str(item.name) + " " + item.is_done_mark + "\n")
            display_list.append(underline + "\n")
        return "".join(display_list)
