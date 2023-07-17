def greeting(name, **kwargs):
    if name:
        return f'Hello {name}'
    else:
        return 'Hello, welcome!'


if __name__ == '__main__':

    name = input("What is your name? :")
    print(greeting(name) + f"\nhow are you?")





