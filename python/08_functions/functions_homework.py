# first way

def remove_duplicates(any_list):
    return list(dict.fromkeys(any_list))

# second way

def remove_duplicates_2(any_list):
    return list(set(any_list))


nums_list = [1, 5, 3, 6, 3, 5, 6, 1]
char_list = ["a", "b", "a", "c", "c"]

print(f"{nums_list = }")
print(f"{char_list =}")
print(f"After sort and delete duplicates: {remove_duplicates(nums_list)}")
print(f"After sort and delete duplicates: {remove_duplicates_2(nums_list)}")
print(f"After sort and delete duplicates: {remove_duplicates(char_list)}")
print(f"After sort and delete duplicates: {remove_duplicates_2(char_list)}")