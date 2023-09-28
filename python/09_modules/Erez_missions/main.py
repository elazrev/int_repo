from first import *
from second import greeting as greet_2
from datetime import date as d
import colorama

color = colorama
color.init(autoreset=True)

print(color.Fore.BLUE + "I'm blue!")
print(color.Fore.GREEN + "if I was green I was die")

date = d.today()


g = greeting("Erez", date)
g2 = greeting("Elazar", date)
h = greet_2("Erez", date)
h2 = greet_2("Elazar", date)

print(g, g2)
print(h, h2)
