import sqlite3


def add_tasks(tasks):
    db = sqlite3.connect("ToDoList")
    cursor = db.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Tasks(id INTEGER PRIMARY KEY, task TEXT)
                ''')
    cursor.executemany(''' INSERT INTO Tasks(task) VALUES(?)''', tasks)
    db.commit()
    db.close()


def main():
    tasks = []
    while True:
        task = input(
            "Please add a task to the To Do List (enter 'end' to finish): ")
        if task == "end":
            break
        tasks.append((task,))

    add_tasks(tasks)


main()

# def end_tasks():
# end_command = input(
#     "Please enter 'end' if you completed your To Do List: ")

# db = sqlite3.connect("ToDoList")
# cursor = db.cursor()

# cursor.execute('''
#                SELECT COUNT(*) FROM Tasks Where remove_task=?, (remove_task,)
#                ''')

# delete_tasks = input(
# "Please enter the name of the task that you wish to remove from the To Do List: ")
