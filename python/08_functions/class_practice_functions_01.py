# # 01 exercise
#
# def get_text_length(name="Hello"):
#     return len(name)
#
#
# print(get_text_length())
#
# my_list = ["hello", "Elazar", "Giraffe"]
#
#
# def get_text_length_in_list(text_list):
#     return sum(list(map(get_text_length, text_list)))
#
#
# print(get_text_length_in_list(my_list))
#
# # 02 exercise
#
# names_list = ["Yoav", "Ron", "Aviva", "Ronen", "Dan", "Galit"]
#
# def len_of_objects_in_list(strings_list):
#     return list(map(lambda x: len(x), strings_list))
#
# def long_names_only(strings_list):
#     min_len = 4
#     return list(filter(lambda x: len(x) > min_len, strings_list))
#
# print(len_of_objects_in_list(names_list))
# print(long_names_only(names_list))
#
# # 03 exercise
# #
# def exponantion(number):
#     return f"{number ** 2 }, {number ** 3}"
#
#
# num = int(input("Enter your number here: "))
# print(exponantion(num))
# a = lambda x, y: f"{x ** 2} {x ** 3} {y ** 5}"
# print(a(num, 3))
# #
# 04 exercise
#
# def calculation(a, b):
#     return f"{a + b}, {a - b}"
#
#
# num1, num2 = input("Enter your two numbers here: ").split()
# res = calculation(int(num1), int(num2))
# print(res)

#
# 05 exercise
#
# def show_employee(name, salary=9000):
#     return f"Name: {name}, Salary: {salary}"
#
# print(show_employee("Erez", 25000))
# print(show_employee("Elazar"))
#

# 06 exercise

# def is_palindrome(user_str):
#     if user_str == user_str[::-1]:
#         return "This is a Palindrome!"
#
#     else:
#         return "This is NOT a Palindrome"
#
# user_input = input("Give me a word: ")
# print(is_palindrome(user_input))

# 07 exercise
#
# def first_and_last(user_list):
#     return [user_list[0], user_list[-1]]
#
# original_list = [5, 10, 15, 20, 251]
# print(first_and_last(original_list))
#


# 08 exercise

# def count_args(*args):
#     return f"{args} => {len(args)}"
#
#
# print(count_args(1, 2, 3))
# print(count_args(1, 2))
# print(count_args(1))
# print(count_args())
#

# 09 exercise

# def check_sum(num_list):
#     if sum(num_list) >= 50:
#         return "verification passed"
#     else:
#         return "not enough"
#
#
# user_input = list(map(lambda x: int(x), input("Enter your numbers here:\n").split()))
# print(check_sum(user_input))

#
# 10 exercise

# def multiply(*args):
#     if len(args) == 0:
#         return f"multiply{args} => 1"
#     else:
#         res = 1
#         for num in args:
#             res *= num
#         return f"multiply{args} => {res}"
#
# print(multiply(1, 2, 3))
# print(multiply(1, 3))
# print(multiply(2))
# print(multiply())
#

# 11 exercise
# def only_one_positive(*numbers):
#     positive_numbers = 0
#     for num in numbers:
#         if num > 0:
#             positive_numbers += 1
#
#     return positive_numbers == 1
#
#
# print(only_one_positive(1, 2))
# print(only_one_positive(-11, 0, -3, 5, -3))
# print(only_one_positive())
