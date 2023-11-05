# Task Number 1 

print( " Task number 1 \n \n ")



import os

# Initialize an empty list to store tasks
tasks = []

# Function to display the to-do list
def display_tasks():
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

# Function to add a task to the to-do list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to mark a task as done
def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print(f"Task '{completed_task}' marked as complete.")
    else:
        print("Invalid task index.")

# Function to remove a task from the to-do list
def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index.")

# Main loop for the application
while True:
    os.system('clear' if os.name == 'posix' else 'cls')  # Clear the terminal screen
    display_tasks()
    
    print("\nOptions:")
    print("1. Add a new task")
    print("2. Mark a task as complete")
    print("3. Remove a task")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        new_task = input("Enter the task: ")
        add_task(new_task)
    elif choice == '2':
        task_index = int(input("Enter the task number to mark as complete: "))
        complete_task(task_index)
    elif choice == '3':
        task_index = int(input("Enter the task number to remove: "))
        remove_task(task_index)
    elif choice == '4':
        break
    else:
        input("Invalid choice. Press Enter to continue...")

print("Thank you for using the To-Do List application!")

# Save tasks to a file (optional)
with open("tasks.txt", "w") as f:
    for task in tasks:
        f.write(task + "\n")