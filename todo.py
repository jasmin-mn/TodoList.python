#  Todo List Program

tasks = []  

def todo():
    global tasks  # Use the global tasks list

    while True:
        # Menu
        print("\nTodo List Menu")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        # Get user choice
        choice = input("Choose an option: ").strip()
        print(f"DEBUG: You entered '{choice}'")  # Debug to check input

        # Option 1: View Tasks
        if choice == "1":
            print("DEBUG: Entered option 1")  # Debug to see if this block runs
            if tasks:
                print("Your tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks added yet.")

        # Option 2: Add Task
        elif choice == "2":
            task = input("Enter a task: ").strip()
            tasks.append(task)
            print(f"'{task}' has been added to the list.")

        # Option 3: Remove Task
        elif choice == "3":
            if tasks:
                try:
                    task_num = int(input("Enter the task number to remove: "))
                    if 0 < task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        print(f"Task '{removed_task}' removed.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks to remove.")

        # Option 4: Exit
        elif choice == "4":
            print("Goodbye!")
            break

        # Invalid option
        else:
            print("Invalid choice. Try again.")

# Run the Todo program
todo()


            