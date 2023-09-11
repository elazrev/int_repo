# 1

# user_input = input("Enter your word: ")
# if user_input.capitalize() == 'Python':
#     print("YES")
# else:
#     print("NO")

# 2

# TOP_LIMIT = 20000
# TAX = 0.13
# salary = int(input("Enter your salary: "))
# if salary > TOP_LIMIT:
#     print(f"after taxes your salary is {salary - salary * TAX}")
# else:
#     print(f"No taxes needed your salary is {salary}")

# 3

# num_1 = int(input("Enter first number: "))
# num_2 = int(input("Enter second number: "))
#
# if num_1 > num_2:
#     print(num_1)
# elif num_1 == num_2:
#     print("You have print the same number")
# else:
#     print(num_2)

# 4

# first_word = input("Enter first word: ")
# second_word = input("Enter second word: ")[::-1]
# equal = first_word == second_word
# match equal:
#     case True:
#         print("YES")
#     case False:
#         print("NO")
#

# 5

# number = int(input("Enter a number: "))
# print("Odd" if number % 2 != 0 else "Even" if number != 0 else "Zero")

# 6

# num_1 = int(input("Enter the first number: "))
# num_2 = int(input("Enter the second number: "))
# if num_1 > num_2:
#     print(f'{num_2} {num_1}')
# else:
#     print(f'{num_1} {num_2}')
#

# 7

# user_input = input("Enter your sentence: ")
# if '?' in user_input:
#     print('Question')
# else:
#     print('Regular')

# 8

# a = input()
# b = input()
# c = input()
# if a == b == c:
#     print(3)
# elif a == b or a == c or b == c:
#     print(2)
# else:
#     print(0)

# 9

# import calendar     #Import the calendar module for prevent overwrite
#
# user_input = int(input("Enter number of month to get the name of it: "))
# if user_input in range(1, 13):
#     print(calendar.month_name[user_input])
# else:
#     print("Invalid month")

# 10

# MIN_CHARS = 7
#
# pwd_1 = input("Enter your password: ")
#
# if len(pwd_1) < MIN_CHARS:
#     print("Short")
# else:
#     pwd_2 = input("Enter your password: ")
#
#     if pwd_1 == pwd_2:
#         print('OK!')
#     else:
#         print('Difference')
#

# 11

# user_experience = int(input("Enter your experience (range of 1-3): "))
# if user_experience not in range(1, 4):
#     print("Invalid Choice!")
# else:
#     if user_experience == 1:
#         print('You are beginner')
#     elif user_experience == 2:
#         print('You are intermediate')
#     else:
#         print('You are an expert!')

# homework #1
#
# value = int(input("Enter an integer value: "))
# if value == 0:
#     print(f"{value = }")
#     # keep zero out of the range
# elif value % 3 == 0 and value % 5 == 0 and value:
#     print("FizzBuzz")
# elif value % 3 == 0 or value % 5 == 0:
#     print("Fizz" if value % 3 == 0 else "Buzz")
# else:
#     print(f'{value = }')
#

# # homework #2
# import calendar
# # Import calendar for save time
#
# year = 2023
# month_num = int(input("Enter a month number: "))
#
# if month_num in range(1, 13):
#     print(f'In {calendar.month_name[month_num]} there is {calendar.monthrange(year, month_num)[1]} days')
# else:
#     print("There is no such month!")
#


