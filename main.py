import sqlite3

db = sqlite3.connect('ToDoList')

tasks = []


while True:
    end_command = input(
        "Please enter 'end' if you completed your To Do List: ")
    if end_command == "end":
        break
    task = input("Please add a task to the To Do List: ")
    tasks.append(task)

print(tasks)

delete_tasks = input(
    "Please enter the name of the task that you wish to remove from the To Do List: ")
