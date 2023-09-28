

upper_number = ''

while not upper_number.isdigit() or int(upper_number) < 30:
    upper_number = input("Enter number higher than 30: ")  # Get input from user
    # if not upper_number.isdigit():
    #     print("Wrong input ENTER ONLY NUMBERS over 30!")
    #     upper_number = input("Try again: ")
    # elif int(upper_number) < 30:
    #     print("The number has to be over 30!")
    #     upper_number = input("Try again: ")


for i in range(int(upper_number) + 1):
    if i % 4 == 0 and i % 7 == 0:
        print("Israel Forever")
    elif i % 4 == 0:
        print("Israel")
    elif i % 5 == 0:
        print("Forever")
    else:
        print(i)







