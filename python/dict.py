import calendar
year = 2023
# days = {1: calendar.monthrange(year, 1)[1],
#         2: calendar.monthrange(year, 2)[1],
#         3: calendar.monthrange(year, 3)[1],
#         4: calendar.monthrange(year, 4)[1],
#         5: calendar.monthrange(year, 5)[1],
#         6: calendar.monthrange(year, 6)[1],
#         7: calendar.monthrange(year, 7)[1],
#         8: calendar.monthrange(year, 8)[1],
#         9: calendar.monthrange(year, 9)[1],
#         10: calendar.monthrange(year, 1)[1],
#         11: calendar.monthrange(year, 1)[1],
#         12: calendar.monthrange(year, 1)[1],
#         }

days_2 = {}

for i in range(1, 13):
    days_2.update({i: calendar.monthrange(year, i)[1]})

user_input = input("Enter number of month: ")
if int(user_input) not in range(1, 13):
    print("Not valid month")
    exit(1)
else:
    print(days_2[int(user_input)])

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}

print(even_dict)