import json
def load_todo_list(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def save_todo_list(todo_list, filename):
    with open(filename, 'w') as f:
        json.dump(todo_list, f)
todo_list = load_todo_list('todo_list.json')
while True:
    print("\nTODO LIST APPLICATION")
    print("1. View TODO list")
    print("2. Add item")
    print("3. Complete item")
    print("4. Exit")
    choice = input("Enter choice (1-4): ")
    if choice == '1':
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. [{item['status']}] {item['task']}")
    elif choice == '2':
        task = input("Enter new task: ")
        todo_list.append({'task': task, 'status': 'Incomplete'})
        save_todo_list(todo_list, 'todo_list.json')
    elif choice == '3':
        index = int(input("Enter index of task to mark as complete: "))
        if 1 <= index <= len(todo_list):
            todo_list[index - 1]['status'] = 'Complete'
            save_todo_list(todo_list, 'todo_list.json')
        else:
            print("Invalid index.")
    elif choice == '4':
        save_todo_list(todo_list, 'todo_list.json')
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")