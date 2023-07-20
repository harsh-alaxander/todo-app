import funcions
import PySimpleGUI as sg

label = sg.Text("type a todo")
input_box = sg.InputText(tooltip="enter a todo")
add_button = sg.Button("Add")

window = sg.Window("my to-do app",layout=[[label],[input_box,add_button]])
window.read()
window.close()
