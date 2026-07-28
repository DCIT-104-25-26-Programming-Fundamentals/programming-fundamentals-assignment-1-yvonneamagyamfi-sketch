def add_task(tasks, task=None):
    if task is None:
        task = input("Enter task: ").strip()
    tasks.append(task)
    print(f'Task added: "{task}"')


def view_tasks(tasks):
    if not tasks:
        print("Your task list is empty.")
        return

    print("Your Tasks:")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")


def delete_task(tasks, task_number=None):
    if not tasks:
        print("Your task list is empty.")
        return

    view_tasks(tasks)
    if task_number is None:
        try:
            task_number = int(input("Enter task number to delete: "))
        except ValueError:
            print("Error: Please enter a valid task number.")
            return

    if task_number < 1 or task_number > len(tasks):
        print("Error: Invalid task number.")
        return

    task = tasks.pop(task_number - 1)
    print(f'Task "{task}" has been removed.')


def print_menu():
    print("\n============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def main():
    tasks = []
    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Please choose a number from 1 to 4.")


if __name__ == "__main__":
    main()
