def menu_driven_todo():
    # Store tasks as dictionaries with 'name' and 'completed' status
    tasks = []
    
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Quit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            task_name = input("Enter the task: ").strip()
            if task_name:
                tasks.append({"name": task_name, "completed": False})
                print(f"Task '{task_name}' added.")
            else:
                print("Task cannot be empty.")
                
        elif choice == "2":
            if tasks:
                print("\nTasks:")
                for i, task in enumerate(tasks, 1):
                    status = "✓" if task["completed"] else "✗"
                    print(f"{i}. [{status}] {task['name']}")
            else:
                print("No tasks found.")
                
        elif choice == "3":
            if tasks:
                print("\nTasks:")
                for i, task in enumerate(tasks, 1):
                    status = "✓" if task["completed"] else "✗"
                    print(f"{i}. [{status}] {task['name']}")
                
                try:
                    task_num = int(input("\nEnter the task number to mark as completed: "))
                    if 1 <= task_num <= len(tasks):
                        if tasks[task_num - 1]["completed"]:
                            print(f"Task '{tasks[task_num - 1]['name']}' is already completed.")
                        else:
                            tasks[task_num - 1]["completed"] = True
                            print(f"Task '{tasks[task_num - 1]['name']}' marked as completed.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks to mark as completed.")
                
        elif choice == "4":
            if tasks:
                print("\nTasks:")
                for i, task in enumerate(tasks, 1):
                    status = "✓" if task["completed"] else "✗"
                    print(f"{i}. [{status}] {task['name']}")
                
                try:
                    task_num = int(input("\nEnter the task number to delete: "))
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        print(f"Task '{removed_task['name']}' deleted.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks to delete.")
                
        elif choice == "5":
            print("Exiting the to-do list. Goodbye!")
            break
            
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu_driven_todo()