import add


def multi(num1, num2):
    a = 0
    for i in range(num2):
        a = add.add(a, num1)
    return a


if __name__ == "__main__":
    print(multi(2, 4))
