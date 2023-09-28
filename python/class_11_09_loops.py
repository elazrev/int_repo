# num = 0
# while not num == 100:
#     num += 2
#     print(num)

# num = 1
# while num < 100:
#     print(num)
#     num +=2
#

# first_row = [i for i in range(1, 10)]
# print(first_row)
#
# for i in range(1, 10):
#     print(i, end="\t")
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print()
#
# for i in range(1, 10):
#     print(i, end="\t")
#     for j in range(1, 10):
#         print("{:3d}".format(i * j), end="\t") # formating
#     print()
#

# my_list = [i for i in range(10, 51, 10)]
# print(my_list)
# print(dict(enumerate(my_list)))
#
# for index, item in enumerate(my_list):
#     print(f"{index+1}. {item} - completed")
# print("\n\n")
#
# my_string = "Elazar"
# for index, item in enumerate(my_string, start=1):
#     print(f"{index}. {item}")


# first practice

words = ['java', 'python', 'javascript', 'php', 'typescript']
enumerated_list = []
for word in enumerate(words, start=1):
    enumerated_list.append(word[::-1])
print(enumerated_list)

# second practice

words_2 = ('attack', 'bless', 'look', 'short', 'monster', 'sound')
for index, word in enumerate(words_2, start=1):
    print(f"Word with index {index} = {word}")

# # homework
# user_input = int(input("Enter your number, it should be greater than 30 : "))
# while not user_input >= 30:
#     print("You entered a low number, it should be grater than 30!!")
#     user_input = int(input("Try again: "))
# for i in range(1, user_input + 1):
#     if i % 4 == 0 and i % 7 == 0:
#         print("Israel Forever")
#     elif i % 4 == 0 or i % 5 == 0:
#         print("Israel" if i % 4 == 0 else "Forever")
#     else:
#         print(i)

# row
for i in range(1, 10):
    print(i, end="\t")
    # column
    for j in range(1, 10):
        print(i * j, end="\t")
    print()