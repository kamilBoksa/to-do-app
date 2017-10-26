from todo_controller import *


def import_ui():
    ui = []
    with open('user_interface.txt') as ui_file:
        for line in ui_file:
            ui.append(line)
    return "".join(ui)


def main():
    print(import_ui())
    handle_ui_choice()


if __name__ == "__main__":
    main()
