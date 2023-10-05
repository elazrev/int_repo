import to_do_items_manager as todo


def task_manager():
    tasks = []
    print(todo.display_menu())
    user_input = ''
    while not user_input == "5":
        user_input = input("Enter your action here: ")
        if int(user_input) not in range(1, 6):
            print("Invalid choice!")
        else:
            match user_input:
                case "1":
                    todo._add_task(tasks)

                case "2":
                    todo._view_tasks(tasks)

                case "3":
                    todo._mark_completed(tasks)

                case "4":
                    todo._delete_task(tasks)





task_manager()