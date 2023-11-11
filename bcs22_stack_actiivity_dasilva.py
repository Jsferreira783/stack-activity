class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print(f'Task "{title}" added successfully.')

    def mark_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True
                print(f'Task "{title}" marked as completed.')
                return
        print(f'Task "{title}" not found.')

    def display_tasks(self):
        if not self.tasks:
            print('No tasks available.')
        else:
            for task in self.tasks:
                status = 'Completed' if task.completed else 'Not Completed'
                print(f'Title: {task.title}, Description: {task.description}, Status: {status}')

if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)
        elif choice == '2':
            title = input("Enter the title of the task to mark as completed: ")
            task_manager.mark_completed(title)
        elif choice == '3':
            task_manager.display_tasks()
        elif choice == '4':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
