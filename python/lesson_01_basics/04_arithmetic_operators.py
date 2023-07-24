"""
Operators in Python:
+ plus => add
- minus => 
* duplicate
/ divide
% modulo
// divide without remain
** power
"""

num_1 = 5
num_2 = 3
str_1 = '*'
strings_list = [
    print(f'{num_1} + {num_2} = {num_1 + num_2}'),   #plus
    print(f'{num_1} - {num_2} = {num_1 - num_2}'),   #minus
    f'{num_1} * {num_2} = {num_1 * num_2}',   #duplicate
    f'{num_1} / {num_2} = {num_1 / num_2}',   #divide
    f'{num_1} % {num_2} = {num_1 % num_2}',   #modulo
    f'{num_1} // {num_2} = {num_1 // num_2}',   #divide without reamain
    f'{num_1} ** {num_2} = {num_1 ** num_2}',   #power
    # Possible arithmetic with chars

    f'{str_1} * {num_2} = {str_1 * num_2}',   #duplicate
    f'{str_1} % {num_2} = {str_1 % num_2}',   #modulo
                ]

def print_if_possible(string):
    try:
        eval_result = eval(string.split('=')[1])  # Evaluate the expression after '='
        print(string + " =", eval_result)
    except:
        print(f'"{string}" is not a legal syntax')


for string in strings_list:
    print(eval(string))