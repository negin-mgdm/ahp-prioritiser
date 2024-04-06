import sqlite3


def add_tasks_to_db(tasks):
    db = sqlite3.connect("ToDoList")
    cursor = db.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Tasks(id INTEGER PRIMARY KEY, task TEXT, priority INTEGER)
                ''')
    cursor.executemany(
        ''' INSERT INTO Tasks(task, priority) VALUES(?, ?)''', tasks,)
    db.commit()
    db.close()


def add_tasks():
    tasks = []
    while True:
        task = input(
            "Please add a task to the To Do List (enter 'end' to finish): ")
        if task == "end":
            break
        tasks.append((task, 0,))

    add_tasks_to_db(tasks)


def main():
    text = ''' 
    1. Add tasks 
    2. Prioritise tasks
    3. View tasks
    '''
    choice = input(text)
    if choice == "1":
        add_tasks()


main()
