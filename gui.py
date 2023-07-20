import funcions
import PySimpleGUI as sg

label = sg.Text("type a todo")
input_box = sg.InputText(tooltip="enter a todo",key='todo')
add_button = sg.Button("Add")

window = sg.Window("my to-do app",
                   layout=[[label],[input_box,add_button]],
                   font=("helvetica",20))

while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = funcions.get_todos()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            funcions.write_todos(todos)

        case sg.WIN_CLOSED:
            break

window.close()
