import PySimpleGUI as psg
import functions

label = psg.Text("Type in a todo")
input_box = psg.InputText(tooltip="Enter todo", key="todo")
add_button = psg.Button("Add")

window = psg.Window('To-do app', layout=[
    [label],
    [input_box, add_button]],
    font=("Helvetica", 20))


while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_list()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_tolist(todos)
        case psg.WIN_CLOSED:
            break

window.close()