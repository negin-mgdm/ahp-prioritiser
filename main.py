import sqlite3
import datetime


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


class TaskService:

    db_context = TaskDbContext()

    def add_tasks(self):
        tasks = []
        while True:
            task = input(
                "Please add a task to the To Do List (enter 'end' to finish): ")
            if task == "end":
                break
            tasks.append((task, 0, "n/a",))

        self.db_context.add_tasks_to_db(tasks)

    def prioritise(self):
        tasks = self.db_context.get_tasks_from_db()
        n = len(tasks)
        priority = [0] * n
        print("Choose which tasks are more important:")
        for i in range(n):
            for j in range(i + 1, n):
                print("A: " + tasks[i][1])
                print("B: " + tasks[j][1])
                choice = input('A or B: ')
                if choice == "A":
                    priority[i] = priority[i] + 1
                else:
                    priority[j] = priority[j] + 1

        for i in range(n):
            self.db_context.update_priorities(tasks[i][0], priority[i])

    def add_due_date(self):
        tasks = self.db_context.get_tasks_from_db()
        n = len(tasks)
        due_date = []
        due_date = input("Please enter a due date (DD-MM-YYYY format): ")
        formatted_date = due_date.strftime("%d-%m-%Y")

    def view_tasks(self):
        tasks = self.db_context.get_tasks_from_db()
        sorted_tasks = sorted(tasks, key=lambda task: task[2], reverse=True)
        for task in sorted_tasks:
            print(f"{task[1]}")

    def remove_tasks(self):
        tasks = self.db_context.get_tasks_from_db()
        for task in tasks:
            print(f"{task[0]}: {task[1]}")

        choice = input(
            "Please enter the id of the task that you wish to remove: ")
        id = int(choice)
        self.db_context.remove_tasks_from_db(id)


def main():
    while True:
        text = ''' 
        1. Add tasks 
        2. Prioritise tasks
        3. View tasks
        4. Remove tasks
        5. Exit
        '''
        task_service = TaskService()
        choice = input(text)
        if choice == "1":
            task_service.add_tasks()
        elif choice == "2":
            task_service.prioritise()
        elif choice == "3":
            task_service.view_tasks()
        elif choice == "4":
            task_service.remove_tasks()
        elif choice == "5":
            break


main()
