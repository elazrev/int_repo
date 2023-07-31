num_list = []
user_choose = 0
while user_choose != '':
    user_choose = input("Enter a number: ")
    if user_choose.isdigit():
        num_list.append(int(user_choose))

average = sum(num_list)/len(num_list)
print(f"The average of the whole numbers you have entered is: {average}")
print(f"The highest num is: {max(num_list)}")
print(f"The lowest num is: {min(num_list)}")
