import funcions
import PySimpleGUI as sg
import time

sg.theme("Black")

clock = sg.Text('',key='clock')
label = sg.Text("type a todo")
input_box = sg.InputText(tooltip="Enter a todo",key='todo')
add_button = sg.Button("Add",size=10)
list_box = sg.Listbox(values=funcions.get_todos(),key='todos',
                      enable_events=True,size=[45,10])

edit_button = sg.Button('Edit')
complete_button = sg.Button("complete")
exit_button = sg.Button("Exit")

window = sg.Window('my to do app',
                   layout=[[clock],
                           [label],
                           [input_box,add_button],
                           [list_box,edit_button,complete_button ],
                           [exit_button]],
                   font=('helvetica',20))


while True:
    event,values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d %Y %H:%M:%S"))




    match event:
        case "Add":
            todos = funcions.get_todos()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            funcions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit=values['todos'][0]
                new_todo=values['todo']

                todos = funcions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo+"\n"
                funcions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("please select item first",font=('Helvetica',20))
        case 'complete':
            try:
                todos_to_complete = values['todos'][0]
                todos =funcions.get_todos()
                todos.remove(todos_to_complete)
                funcions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value=" ")
            except IndexError:
                sg.popup("please select item first", font=('Helvetica', 20))


        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break


window.close()