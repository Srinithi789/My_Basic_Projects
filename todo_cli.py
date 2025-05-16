# Simple To-Do List App using file storage

def show_tasks():
    """Display all current tasks from the file."""
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
            else:
                print("No tasks found!")
    except FileNotFoundError:
        print("No task file found. Start adding tasks!")

def add_task(task):
    """Add a new task to the file."""
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added!")

def delete_task(index):
    """Delete a task by its number in the list."""
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"Deleted: {removed.strip()}")
        else:
            print("Invalid task number!")
    except FileNotFoundError:
        print("No tasks to delete!")

def main():
    """Main loop of the program."""
    while True:
        print("\nTo-Do List Options:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "3":
            show_tasks()
            try:
                number = int(input("Enter the task number to delete: ")) - 1
                delete_task(number)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
