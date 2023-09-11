#user_input_1 = int(input())
#user_input_2 = int(input())
#print(tuple(range(user_input_1, user_input_2 + 1)))

my_tuple = tuple(range(101))
print(f"{my_tuple[44] =}\n{my_tuple[-9] = }\n{my_tuple[-1] = }")
my_tuple_2 = tuple(range(21))
print(my_tuple_2[::-1])
my_tuple_3 = tuple(range(26))
print(f"avarage of my third tuple is {sum(my_tuple_3) / len(my_tuple_3)}")

my_tuple_4 = tuple(range(10, 41, 10))
print(my_tuple_4)
a, b, c, d = [* my_tuple_4]
print(a)
print(b)
print(c)
print(d)
nums_list = list(range(12))
print(nums_list[::1])

tuple1 = tuple(range(11, 67, 11))
tuple2 = tuple1[3:5]
print(tuple2)

tuple3 = (11, [22, 33], 44, 55)
tuple3[1][0] = 222
print(tuple3)

tuple4 = (11, [22, 33], 44, 55)
tuple4 = list(tuple4)
replace
