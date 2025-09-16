tasks = []

while True:
    print("\nTo-Do List Menu")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Check Off Task")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Select an option ('1,' '2,' etc.): ")

    # LOGIC FOR "1. VIEW TASKS"
    if choice == '1':
        if not tasks:
            print("You have not assigned any tasks yet.")
        else:
            print(tasks)

    # LOGIC FOR "2. ADD TASK"
    elif choice == '2':
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        deadline = input("Enter task deadline: ")
        tasks.append({'title': title, 'description': description, 'deadline': deadline, 'done': False})
        print("Task added successfully.")

    # LOGIC FOR "3. CHECK OFF TASK"
    elif choice == '3':
        if not tasks:
            print("No tasks to check off.")
        else:
            for idx, task in enumerate(tasks, 1):
                status = "[X]" if task['done'] else "[ ]"
                print(f"{idx}. {status} {task['title']} - {task['description']} (Due: {task['deadline']})")
            try:
                task_num = int(input("Enter the task number to check off: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]['done'] = True
                    print("Task checked off.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    # LOGIC FOR "4. REMOVE TASK"
    elif choice == '4':
        if not tasks:
            print("No tasks to remove.")
        else:
            for idx, task in enumerate(tasks, 1):
                status = "[X]" if task['done'] else "[ ]"
                print(f"{idx}. {status} {task['title']} - {task['description']} (Due: {task['deadline']})")
            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"Removed task: {removed_task['title']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    # LOGIC FOR "5. EXIT"
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
