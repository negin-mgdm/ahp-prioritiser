from TaskDbContext import TaskDbContext


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
