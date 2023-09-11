a = "hello world"
b = a.split()
print(id(a))
print(f"b-ID {id(b)}")
print(a, "\n", b)
print(type(b))

print(a[3])
print(b[0])

#a[3] = "G"
a = a.replace('ll', "RE")
print(a)
print(id(a))
print(a)
b[0] = "Erez"
print(f"b-ID {id(b)}")
print(b)
