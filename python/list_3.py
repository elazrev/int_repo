g = list(("Erez", "Apple", "Rachamim"))
print(g)

more_names = ["dan", "gal", "ben"]

g += more_names
g += ["beni"]

g.append(1)
g.append(True)
g.append([1, 2, 3])
g.append([1, 5, 3])


print(g)
print(len(g))

print(g[::-1])
print(g[0:-1:2])

go = g[::-1]
print(id(g))
print(id(go))
