tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print("-----Task Added -------")
    print(f"Task: {task} added")
    print("-----------------------")

def display_tasks():
    if not tasks:
        print("-----Tasks Displayed -------")
        print("Your to-do list is empty!")
        print("----------------------------")
        return

    print("-----Tasks Displayed -------")
    for idx, task_data in enumerate(tasks):
        status = "[X]" if task_data["completed"] else "[ ]"
        print(f"{idx + 1}. {status} {task_data['task']}")
    print("----------------------------")

def delete_task():
    if not tasks:
        print("Your to-do list is empty. Nothing to delete!")
        return

    display_tasks()
    try:
        task_index_to_delete = int(input("Enter the number of the task to delete: "))
        if 1 <= task_index_to_delete <= len(tasks):
            deleted_task = tasks.pop(task_index_to_delete - 1)
            print(f"Task '{deleted_task['task']}' deleted from the list.")
        else:
            print("Invalid task number. Please enter a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def complete_task():
    if not tasks:
        print("Your to-do list is empty. Nothing to complete!")
        return

    display_tasks()
    try:
        task_index_to_complete = int(input("Enter the number of the task to mark as complete: "))
        if 1 <= task_index_to_complete <= len(tasks):
            tasks[task_index_to_complete - 1]["completed"] = True
            print(f"Task '{tasks[task_index_to_complete - 1]['task']}' marked as complete.")
        else:
            print("Invalid task number. Please enter a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        print("\nTo do list App")
        print("1. Add Task")
        print("2. Display Task")
        print("3. Delete Task")
        print("4. Complete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            complete_task()
        elif choice == '5':
            print("Thanks for using application")
            break
        else:
            print("Invalid input. Try Again.")

if __name__ == "__main__":
    main()