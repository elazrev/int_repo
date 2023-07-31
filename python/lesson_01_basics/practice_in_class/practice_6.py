user_choose = input("Which temperature would you like to convert?\n"
                    "C -> celsius/ F -> Fahrenheit")

if user_choose.lower() == 'c':
    fahrenheit = float(input())
    print((fahrenheit - 32) * 5 / 9)
elif user_choose.lower() == 'f':
    celsius = float(input())
    print(celsius * 1.8 + 32 )
else:
    print("you choose wrong option\n\tBye")