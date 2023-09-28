# def double_num(num):
#     return num * 2
#
# num_list = [1, 2, 3, 4, 5, 6]
#
# double_list = []
#
# for num in num_list:
#     double_list.append(double_num(num))
#
# print(num_list)
# print(double_list)
#
# print(map(double_num, num_list))
# print(list(map(double_num, num_list)))
#
# def power_num(num):
#     return num ** 2
#
# num_list_2 = [1, 2, 3, 1, 5, 7]
# print(list(map(lambda x: x ** 2, num_list_2)))
#

# def name_len(name):
#     """This func will power every number"""
#     return len(name)
#
#
# names_list = ["Yoav", "Ron", "Aviva", "Ronen", "Dan", "Galit"]
# print(list(map(lambda x: len(x), names_list)))
# print(list(filter(lambda x: len(x) > 4, names_list)))

# long_names = []
# for name in names_list:
#     if len(name) > 4:
#         long_names.append(name)
#
# print(long_names)


def hello(name):
    if name:
        return f"Hello {name}"
    else:
        return "Hello dear friend"


user_input = input("Enter your name: ")
print(hello(user_input))