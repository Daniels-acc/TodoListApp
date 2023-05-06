import datetime
import os
import pytz

folder_path_src = (r"C:\Users\daniel.gluhak\OneDrive - Q Experience\Documents\python-workspace\50-days-20-apps\app_1")
file_list = os.listdir(folder_path_src)

# --------------------------------------

# --------------------------------------
# functions:
def get_list():
    with open('todo_list.txt', 'r') as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local

def set_list():
    with open('todo_list.txt', 'w') as file:
        file.writelines(todo_list)
    return todo_list

# --------------------------------------

while True:

    user_input = input('Enter: "add", "show", "edit, "delete", "complete" : ')
    user_input = user_input.strip()


    #     add
    if user_input.startswith("add") or user_input.startswith("new"):
        add_todo = user_input[4:]

        todo_list = get_list()
            # print(f"Successfully added '{add_todo}' to a list.")
        todo_list.append(add_todo + "\n")

        with open('date_log.txt', 'a') as file_date:
            file_date.writelines(f"{str(datetime.datetime.now(pytz.timezone('Europe/Zagreb')))} - added to: list" + "\n")


    #     show
    elif user_input.startswith("show"):

        todo_list = get_list()
        for i, item in enumerate(todo_list):
            item = item.strip("\n")
            print(f"{i + 1}. {item} ")


    #   edit
    elif user_input.startswith("edit"):
        try:
            todo_list = get_list()
            num_edit = int(user_input[5:]) - 1
            old_todo = todo_list[num_edit]
            confirm = input(f"Are you sure you want to edit {old_todo.strip()} ? (y/n): ")
            new_todo = input("Enter new todo: ").capitalize()
            todo_list[num_edit] = new_todo + "\n"

            if confirm == 'y'.lower():
                with open('todo_list.txt', 'w') as file:
                    file.writelines(todo_list)
                    print(f"{file.name} has been edited. Item number {num_edit+1}: {todo_list[num_edit]}")

                with open('date_log.txt', 'a') as file_date:
                    file_date.writelines(f"{str(datetime.datetime.now())} - edited: {file.name}"+"\n")
            else:
                print('Nothing edited.')
        except ValueError:
            print("Input not valid.")


    #     delete
    elif user_input.startswith("delete"):
        # 1. iterates and shows items in a file imported as -> todo_list
        get_list()
        for i, item in enumerate(todo_list):
            item = item.strip("\n")
            row_item = (f"{i + 1}. {item} ")
            print(row_item)
        # 2. manipulating imported
        num_del = int(input("Enter number to delete: ")) - 1
        deleted_todo = todo_list.pop(num_del)
        confirm = input(f'Are you sure you want to delete {deleted_todo} (y/n): ')
        # 3. confirmation and overwriting todo_list list back to a todo_list.txt file
        if confirm.lower() == 'y':
            with open('todo_list.txt', 'w') as file:
                for todo in todo_list:
                    file.write(todo)
                print('Todo deleted')
        else:
            print('Todo deletion canceled')


    #     complete
    elif user_input.startswith("complete"):

        todo_list = get_list()
        for i, item in enumerate(todo_list):
            item = item.strip("\n")
            print(f"{i + 1}. {item} ")

        completed_todo = int(user_input[9:]) -1
        new_todo = todo_list.pop(completed_todo)

        with open('completed_list.txt', 'a') as file:
            file.write(new_todo)
        message = f"Todo {new_todo.strip()} was removed from a list."
        print(message)
        # -- iterates through a new_todo list and writes remaining items in the todo_list.txt
        with open('todo_list.txt', 'w') as file:
            for item in todo_list:
                file.writelines(item)
        message = f"Todo {new_todo.strip()} was added to a list."
        print(message)


    #   exit
    elif 'exit' in user_input:
        break


    #   rerun
    else:
        print('Type: add, show, edit, delete, complete or exit.')