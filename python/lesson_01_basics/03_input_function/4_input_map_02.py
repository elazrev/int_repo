whole_input = input("Enter five scores: ")
whole_input_split = whole_input.split()

# Using a list comprehension to create the score labels
scores = [f'score_{i+1}' for i in range(len(whole_input_split))]

# Using a dictionary comprehension to create the scores_dict
scores_dict = {label: int(score) for label, score in zip(scores, whole_input_split)}

print(scores_dict)