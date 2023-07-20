from funcions import get_todos,write_todos

import time
row = time.strftime("%b %d %Y %H:%M:%S")
print("it is",row)
while True:
    user_action = input("type add or show or exit :")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]


        todos = get_todos()

        todos.append(todo + '\n')


        write_todos(todos)
    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1


            todos = get_todos()

            new_todo = input("new todo")
            todos[number] = new_todo + '\n'


            write_todos(todos)
        except ValueError:
            print("could not convert string to list")
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])


            todos= get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)


            write_todos(todos)
            message = f"{todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("that not type of number")




    elif user_action.startswith("exit"):
        break

    else:
        print("hey type anythings")

print("bye")
