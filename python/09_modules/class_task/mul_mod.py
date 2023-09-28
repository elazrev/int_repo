from add_mod import add


def mul(num1, num2):
    mul_stage = 0
    for i in range(int(num2)):
        mul_stage += add(0, num1)
    return mul_stage


if __name__ == "__main__":
    print(mul(2, 8))