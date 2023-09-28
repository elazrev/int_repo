from mul_mod import mul


def digit_validation(string):
    nums_list = string.split()
    if not len(nums_list) == 2:
        return False
    for char in nums_list:
        if not char.isdigit():
            return False
    return True


if __name__ == "__main__":

    user_input = ' '
    while not user_input == "":
        user_input = input("Enter your two numbers here:\n")
        if digit_validation(user_input):
            num1, num2 = list(map(lambda x: int(x), user_input.split()))
            print(f"{num1} X {num2} = {mul(num1, num2)}")
        else:
            print("invalid input")
