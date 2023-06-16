my_list = [3, 3, 2, 3, 3, 2, 3, 2]
indices = {}

for index, value in enumerate(my_list):
    if value in [3, 2, 1] and value not in indices:
        indices[value] = index

print(indices)