def read(file="todos.txt"):
    with open(file, "r") as file:
        todos = file.readlines()
    return todos


def write(todos, file="todos.txt"):
    with open(file, "w") as filename:
        filename.writelines(todos)
