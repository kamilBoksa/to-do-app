class ToDoItem:

    def __init__(self, name, description, is_done=False):
        self.name = name
        self.description = description
        self.is_done = is_done

    def change_task_name(self, new_name):
        self.name = new_name

    def change_task_description(self, new_description):
        self.description = new_description

    def mark_item(self):
        self.is_done = True
