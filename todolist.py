# PSEUDOCODE FOR TO-DO LIST APP
# 1. Create an empty list to store tasks
# 2. Add a task to the list
# 3. Add a description and deadline to the task
# 4. Check off task from the list
# 5. Remove a task from the list

# SIMPLE TO-DO LIST PROGRAM
import time
import sys

# INITIAL SETUP
tasks = []
while True:
	print("\n-=-=-=-=-=-=-=-=-=-")
	print("\nTo-Do List App")
	print("1. Show tasks")
	print("2. Add task")
	print("3. Check off task")
	print("4. Remove task")
	print("5. Quit")
	choice = input("\nChoose an option (1, 2, 3...): ")

	# LOGIC FOR "1. SHOW TASKS"
	if choice == '1':
		if not tasks:
			print("No tasks yet!")
		else:
			for idx, task in enumerate(tasks, 1):
				status = "[X]" if task['done'] else "[ ]"
				print(f"{idx}. {status} {task['title']} - {task['desc']} (Due: {task['deadline']})")

	# LOGIC FOR "2. ADD TASK"
	elif choice == '2':
		title = input("Task title: ")
		desc = input("Description: ")
		deadline = input("Deadline: ")
		tasks.append({'title': title, 'desc': desc, 'deadline': deadline, 'done': False})
		print("Task added!")

	# LOGIC FOR "3. CHECK OFF TASK"
	elif choice == '3':
		if not tasks:
			print("No tasks to check off!")
		else:
			for idx, task in enumerate(tasks, 1):
				status = "[X]" if task['done'] else "[ ]"
				print(f"{idx}. {status} {task['title']} - {task['desc']} (Due: {task['deadline']})")
			try:
				num = int(input("Enter task number to check off: "))
				if 1 <= num <= len(tasks):
					tasks[num-1]['done'] = True
					print("Task checked off!")
				else:
					print("Invalid task number.")
			except ValueError:
				print("Please enter a valid number.")

	# LOGIC FOR "4. REMOVE TASK"
	elif choice == '4':
		if not tasks:
			print("No tasks to remove!")
		else:
			for idx, task in enumerate(tasks, 1):
				status = "[X]" if task['done'] else "[ ]"
				print(f"{idx}. {status} {task['title']} - {task['desc']} (Due: {task['deadline']})")
			try:
				num = int(input("Enter task number to remove: "))
				if 1 <= num <= len(tasks):
					removed = tasks.pop(num-1)
					print(f"Removed task: {removed['title']}")
				else:
					print("Invalid task number.")
			except ValueError:
				print("Please enter a valid number.")
	
	# LOGIC FOR "5. QUIT"
	elif choice == '5':
		print("Goodbye!")
		break
	else:
		print("Invalid choice. Please try again.")
