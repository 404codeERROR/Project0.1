# todo_list.py

todo_list = []

def show_tasks():
    if not todo_list:
        print("📝 Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(todo_list, 1):
            status = "✅" if task['done'] else "❌"
            print(f"{idx}. {task['task']} {status}")

def add_task():
    task = input("Enter your task: ")
    todo_list.append({'task': task, 'done': False})
    print("Task added! 💪")

def mark_done():
    show_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(todo_list):
            todo_list[index]['done'] = True
            print("Marked as done ✅")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number 😅")

def delete_task():
    show_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(todo_list):
            removed = todo_list.pop(index)
            print(f"Deleted task: {removed['task']} 🗑")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number 😅")

def main():
    while True:
        print("\n=== TO-DO MENU ===")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Pick an option: ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Later! 👋")
            break
        else:
            print("Not a valid option fam 😬")

if _name_ == "_main_":
    main()