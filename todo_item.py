class ToDoItem:

    def __init__(self, name, description, is_done=False):
        self.name = name
        self.description = description
        self.is_done = is_done
        self.is_done_mark = "[ ]"

    def change_task_name(self, new_name):
        self.name = new_name

    def change_task_description(self, new_description):
        self.description = new_description

    def mark_item(self):
        self.is_done = True
        self.is_done_mark = "[x]"

    def unmark_item(self):
        self.is_done = False
        self.is_done_mark = "[ ]"

    def __str__(self):
        return self.name + " - " + self.description + " - " + self.is_done_mark
