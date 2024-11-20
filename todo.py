todo_list = []

def display_menu():
    """Displays the menu options."""
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

def add_task():
    """Add a new task to the list."""
    task = input("Enter the task you want to add: ")
    todo_list.append(task)
    print(f"Task '{task}' added successfully.")

def remove_task():
    """Remove a task from the list."""
    view_tasks()
    try:
        task_index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_index < len(todo_list):
            removed_task = todo_list.pop(task_index)
            print(f"Task '{removed_task}' removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks():
    """Display all tasks in the list."""
    if len(todo_list) == 0:
        print("No tasks in the to-do list.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def main():
    """Main function to run the to-do list program."""
    while True:
        display_menu()
        choice = input("Choose an option (1/2/3/4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Exiting the To-Do List program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
