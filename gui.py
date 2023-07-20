import funcions
import PySimpleGUI as sg

label = sg.Text("type a todo")
input_box = sg.InputText(tooltip="enter a todo",key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=funcions.get_todos(),key="todos",
                      enable_events=True,size=[45,10])

edit_button = sg.Button("Edit")

window = sg.Window("my to-do app",
                   layout=[[label],[input_box,add_button],[list_box,edit_button]],
                   font=("helvetica",20))

while True:
    event,values = window.read()
    print(1,event)
    print(2,values)
    print(3,values['todos'])
    match event:
        case 'Add':
            todos = funcions.get_todos()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            funcions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = funcions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index]=new_todo
            funcions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])





        case sg.WIN_CLOSED:
            break

window.close()

