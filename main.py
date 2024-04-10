from TaskService import TaskService


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
