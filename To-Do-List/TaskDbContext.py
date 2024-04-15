import sqlite3


class TaskDbContext:

    def add_tasks_to_db(self, tasks):
        db = sqlite3.connect("ToDoList")
        cursor = db.cursor()
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Tasks(id INTEGER PRIMARY KEY, task TEXT, priority INTEGER, "due date" TEXT)
                    ''')
        cursor.executemany(
            ''' INSERT INTO Tasks(task, priority, "due date") VALUES(?, ?, ?)''', tasks,)
        db.commit()
        db.close()

    def get_tasks_from_db(self):
        db = sqlite3.connect("ToDoList")
        cursor = db.cursor()
        cursor.execute('''
                    SELECT * FROM Tasks''')
        tasks = cursor.fetchall()
        db.commit()
        db.close()
        return tasks

    def update_priorities(self, id, priority):
        db = sqlite3.connect("ToDoList")
        cursor = db.cursor()
        cursor.execute('''UPDATE Tasks SET priority = ? WHERE id = ?
                    ''', (priority, id))
        db.commit()
        db.close()

    def remove_tasks_from_db(self, id):
        db = sqlite3.connect("ToDoList")
        cursor = db.cursor()
        cursor.execute('''DELETE FROM Tasks WHERE id = ?
                    ''', (id,))
        db.commit()
        db.close()
