def _add(x, y):
    return f"{x}+{y} = {x + y}"

def _subtract(x, y):
    return f"{x}-{y} = {x - y}"

def _multiply(x, y):
    return f"{x}X{y} = {x * y}"

def _divide(x, y):
    return f"{x}÷{y} = {x / y}"

def calculate():

    x = input("Add your first number: ")
    while not x.isdigit():
        x = input("wrong choice try again\nEnter the first number: ")
    y = input("Add your second number: ")
    while not y.isdigit():
        y = input("wrong choice try again\nEnter the second number: ")
    x, y = int(x), int(y)
    operation = input("What is your operation?: ")

    match operation:
        case "+":
            return _add(x, y)

        case "-":
            return _subtract(x, y)

        case "*":
            return _multiply(x, y)

        case "/":
            return _divide(x, y)

        case "exit":
            exit(0)

        case _:
            print("You choose wrong operator!")
            return False


if __name__ == "__main__":
    print(calculate())