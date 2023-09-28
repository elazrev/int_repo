from mul import multi


while True:
    a = input("")
    b = input("")
    if a == '' or b == '':
        exit(1)

    print(multi(int(a), int(b)))