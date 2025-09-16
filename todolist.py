# PSEUDOCODE FOR TO-DO LIST APP
# 1. Create an empty list to store tasks
# 2. Add a task to the list
# 3. Add a description and deadline to the task
# 4. Check off task from the list
# 5. Remove a task from the list


# Simple To-Do List App
import time
import sys

tasks = []
while True:
	print("\nTo-Do List App")
	print("1. Show tasks")
	print("2. Add task")
	print("3. Check off task")
	print("4. Remove task")
	print("5. Stopwatch")
	print("6. Quit")
	choice = input("Choose an option: ")

	if choice == '1':
		if not tasks:
			print("No tasks yet!")
		else:
			for idx, task in enumerate(tasks, 1):
				status = "[X]" if task['done'] else "[ ]"
				print(f"{idx}. {status} {task['title']} - {task['desc']} (Due: {task['deadline']})")

	elif choice == '2':
		title = input("Task title: ")
		desc = input("Description: ")
		deadline = input("Deadline: ")
		tasks.append({'title': title, 'desc': desc, 'deadline': deadline, 'done': False})
		print("Task added!")

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


	elif choice == '5':
		print("\nStopwatch started. Press Enter to stop.")
		start = time.time()
		import msvcrt
		try:
			while True:
				elapsed = time.time() - start
				mins, secs = divmod(int(elapsed), 60)
				millis = int((elapsed - int(elapsed)) * 1000)
				timer = f"{mins:02d}:{secs:02d}.{millis:03d}"
				print(f"\rElapsed time: {timer}   ", end="", flush=True)
				if msvcrt.kbhit():
					if msvcrt.getch() == b'\r':  # Enter key
						break
				time.sleep(0.01)
		except KeyboardInterrupt:
			pass
		print("\nStopwatch stopped.")

	elif choice == '6':
		print("Goodbye!")
		break
	else:
		print("Invalid choice. Please try again.")
