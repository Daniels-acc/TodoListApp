def add():
    num = int(input("Enter how many items you want to add: "))
    for i in range(num):
        add_todo = input("Enter a todo: ").capitalize() + "\n"
        with open('todo_list.txt', 'a') as random_file:
            random_file.write(add_todo)


# --------------------------------------
def complete():
    with open('todo_list.txt', 'r') as file:
        todo_list = file.readlines()
        for i, item in enumerate(todo_list):
            item = item.strip("\n")
            row_item = (f"{i + 1}. {item} ")
            print(row_item)

    # user input & deleting completed
    completed_todo = int(input("Pick a completed item: ")) - 1
    new_todo = todo_list.pop(completed_todo)

    # -- create and append item to complete_list.txt
    with open('completed_list.txt', 'a') as file:
        file.write(new_todo)

    # -- iterates through a new_todo list and writes remaining items in the todo_list.txt
    with open('todo_list.txt', 'w') as file:
        for item in todo_list:
            file.writelines(item)


# --------------------------------------
def show():
    with open('todo_list.txt', 'r') as file:
        todo_list = file.readlines()
        for i, item in enumerate(todo_list):
            item = item.strip("\n")
            row_item = (f"{i+1}. {item} ")
            print(row_item)

# --------------------------------------
def edit():
    # print(f"Items to edit: {show()}: ")
    show()
    num_edit = int(input("Number of todo to edit: ")) - 1

    with open('todo_list.txt', 'r') as file:
        todo_list = file.readlines()
        new_todo = input("Enter new todo: ").capitalize()
        todo_list_old = todo_list[num_edit]
        todo_list[num_edit] = new_todo + "\n"

    confirm = input(f"Are you sure you want to edit {todo_list_old.strip()} ? (y/n): ")

    if confirm == 'y'.lower():
        with open('todo_list.txt', 'w') as file:
            file.writelines(todo_list)
            print(f"{todo_list_old.strip()} has been edited. New value: {todo_list[num_edit]}")
    else:
        print('Nothing edited.')

# --------------------------------------
def delete():
    # 1. iterates and shows items in a file imported as -> todo_list
    with open('todo_list.txt', 'r') as file:
        todo_list = file.readlines()
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


while True:
    user_input = input('Enter: "add", "show", "edit, "delete", "complete" : ')

    match user_input:
        case 'add':
            add()
        case 'show':
            show()
        case 'edit':
            edit()
        case 'delete':
            delete()
        case 'complete':
            complete()