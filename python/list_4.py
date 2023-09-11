my_num_lst = []
my_names_lst = []

my_num_lst.append(1)
my_num_lst.append(2)
my_num_lst.append(2)
my_num_lst.append(2)
my_num_lst.append(20)
my_num_lst.append(-1)
my_num_lst.append(-60)

print(my_num_lst)

my_names_lst += ["Erez", "Yoel", "Alex"]
my_names_lst += ["Alma", "Yulanda", "Yafa"]

print(my_names_lst)
print(my_num_lst.count(2))
print(my_names_lst.count("Erez"))
print("before")

print(id(my_names_lst))
print(my_names_lst)

print("after")
print(id(my_names_lst))

num = 1
print(num)
num = tuple(f"{num}")
print(num)

