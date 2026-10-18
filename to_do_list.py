"""Simple To-Do List - CEIS150 Python project."""


def show_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
        return

    print("\nYour To-Do List:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def main():
    tasks = []

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a completed task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            task = input("Enter a new task: ").strip()
            if task:
                tasks.append(task)
                print("Task added!")
            else:
                print("Please enter a task.")
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                selection = input("Enter the task number to remove: ").strip()
                if selection.isdigit() and 1 <= int(selection) <= len(tasks):
                    removed = tasks.pop(int(selection) - 1)
                    print(f"Completed task removed: {removed}")
                else:
                    print("Invalid task number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
