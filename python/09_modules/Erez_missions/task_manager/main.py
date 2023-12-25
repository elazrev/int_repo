import to_do_items_manager as todo


def task_manager():
    tasks = []
    print(todo.display_menu())
    user_input = ''
    while not user_input == "5":
        user_input = input("Enter your action here: ")
        if user_input.isdigit():
            if int(user_input) not in range(1, 6):
                print("Invalid choice!")
            elif int(user_input) in range(2, 5) and len(tasks) == 0:
                print("You have to add tasks for using this operation...")
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
        else:
            print("It has to be a number")





task_manager()