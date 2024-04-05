class Todolist:
    def __init__(self):
        self.task=[]
    
    def add_task(self, task):
        self.task.append(task)
        print("Task added successfully.")

    def remove_task(self, task):
        if task in self.task:
            self.task.remove(task)
            print("Task removed successfully.")
        else:
            print("Task not found.")

    def display_task(self, task):
        if self.task:
            print("Your To-Do List:")
            for index, task in enumerate(self.task, start=1):
                print(f"{index}. {task}")
        else:
            print("Your To-Do List is empty.")
        
def main():
    todo_list = Todolist()

    while True:
        print("\n========== To-Do List Application ==========")
        print("1. Add task")
        print("2. Remove task")
        print("3. View task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.display_task(task)
        elif choice == '4':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
if __name__ == "__main__":
    main()