my_lst = [11, 12, 13, 14, "Erez", True, 1.56, [1, 2]]
print(my_lst)

my_lst[0] = 99
my_lst[-1] = "Hello"

print(my_lst)
print(type(my_lst[5]))
print(my_lst)
a = str(my_lst[1])
print(a.isdigit())

print(len(my_lst))
print("Erez" in my_lst)
print(15 in my_lst)

new_lst = ["Erez", "Shimon", "Moshe", "Alex", "elazar"]
sort_new_lst = sorted(new_lst, reverse=True)
print(sort_new_lst)

