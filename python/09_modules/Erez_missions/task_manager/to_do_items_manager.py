import colorama
from colorama import Back, Style


def display_menu():
    menu = f"Task Manager Menu\n1.Add a new task\n2.View all task\n3.Mark a task as completed\n4.Delete a task\n5.Exit"
    return menu


def _add_task(tasks: list):
    task = input("Enter your task here: ")
    tasks.append({"task": task, "status": False})
    print(f"Task successfully added!")
    return True


def _view_tasks(tasks: list):
    colorama.init(autoreset=True)
    for i in range(len(tasks)):
        tasks_text = f"{i + 1}.{tasks[i]['task']}"
        print(Back.GREEN + tasks_text if tasks[i]['status'] else tasks_text)


def _mark_completed(tasks: list):
    user_input = input("Enter the completed task number: ")

    while True:
        if user_input.isdigit() and int(user_input) - 1 in range(len(tasks)):
            tasks[int(user_input) - 1]['status'] = True
            break
        else:
            print('Invalid choice, Try again')
            user_input = input("Enter your choice: ")


def _delete_task(tasks: list):
    user_input = input("Enter the the task number to delete: ")

    while True:
        if user_input.isdigit() and int(user_input) - 1 in range(len(tasks)):
            del_task = tasks.pop(int(user_input) - 1)
            print(f'{del_task["task"]} has deleted!')
            break
        else:
            print('Invalid choice, Try again')
            user_input = input("Enter your choice: ")


if __name__ == "__main__":
    print(display_menu())


