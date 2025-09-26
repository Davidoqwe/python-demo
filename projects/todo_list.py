tasks = []

while True:
    print("\nTasks:", tasks)
    action = input("Add/Remove/Exit: ").lower()

    if action == "add":
        task = input("Enter task: ")
        tasks.append(task)
    elif action == "remove":
        task = input("Task to remove: ")
        if task in tasks:
            tasks.remove(task)
        else:
            print("Task not found.")
    elif action == "exit":
        break
    else:
        print("Invalid input.")
