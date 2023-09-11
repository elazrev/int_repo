#a, b = map(int, input("Insert your resolution here: ").split())

#print(f"Screen Resolution: {a} x {b}.\nTotal Resolution of pixels = {a * b}")


list_2 = [f"a+{i}" for i in range(10)]
print(list_2)
print(id(list_2))
list_2[3] = "4"
list_2[3] = "a+6"
print(list_2)
print(sorted(set(list_2)))