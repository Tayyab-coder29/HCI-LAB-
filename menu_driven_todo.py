#!/usr/bin/env python3
"""
Menu-Driven To-Do List with Task Completion
Features: Add, View, Delete, Mark as Completed, and View Completed Tasks
"""

def menu_driven_todo():
    tasks = []  # List of tuples: (task_name, is_completed)
    
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. View Completed Tasks")
        print("6. Quit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            task = input("Enter the task: ").strip()
            if task:
                tasks.append({"name": task, "completed": False})
                print(f"Task '{task}' added.")
            else:
                print("Task cannot be empty.")
        
        elif choice == "2":
            if tasks:
                print("\n--- All Tasks ---")
                for i, task in enumerate(tasks, 1):
                    status = "✓" if task["completed"] else "✗"
                    print(f"{i}. [{status}] {task['name']}")
            else:
                print("No tasks found.")
        
        elif choice == "3":
            if tasks:
                print("\n--- Current Tasks ---")
                for i, task in enumerate(tasks, 1):
                    status = "✓" if task["completed"] else "✗"
                    print(f"{i}. [{status}] {task['name']}")
                
                try:
                    task_num = int(input("Enter the task number to delete: "))
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        print(f"Task '{removed_task['name']}' deleted.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No tasks to delete.")
        
        elif choice == "4":
            if tasks:
                # Show only incomplete tasks
                incomplete_tasks = [(i, task) for i, task in enumerate(tasks) if not task["completed"]]
                
                if incomplete_tasks:
                    print("\n--- Incomplete Tasks ---")
                    for idx, (i, task) in enumerate(incomplete_tasks, 1):
                        print(f"{i + 1}. {task['name']}")
                    
                    try:
                        task_num = int(input("Enter the task number to mark as completed: "))
                        if 1 <= task_num <= len(tasks):
                            if not tasks[task_num - 1]["completed"]:
                                tasks[task_num - 1]["completed"] = True
                                print(f"Task '{tasks[task_num - 1]['name']}' marked as completed!")
                            else:
                                print("Task is already completed.")
                        else:
                            print("Invalid task number.")
                    except ValueError:
                        print("Please enter a valid number.")
                else:
                    print("All tasks are already completed!")
            else:
                print("No tasks found.")
        
        elif choice == "5":
            completed_tasks = [task for task in tasks if task["completed"]]
            if completed_tasks:
                print("\n--- Completed Tasks ---")
                for i, task in enumerate(completed_tasks, 1):
                    print(f"{i}. ✓ {task['name']}")
            else:
                print("No completed tasks.")
        
        elif choice == "6":
            print("Exiting the to-do list. Goodbye!")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu_driven_todo()
