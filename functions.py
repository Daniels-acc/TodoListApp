def get_list(filepath="todo_list.txt"):
    """ Read a text file and returns the list of items """
    with open(filepath, 'r') as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local

def write_tolist(user_entry, filepath="todo_list.txt"):
    """ Open a text file: enter filepath and write user input to a list """
    with open(filepath, 'w') as file_local:
        file_local.writelines(user_entry)