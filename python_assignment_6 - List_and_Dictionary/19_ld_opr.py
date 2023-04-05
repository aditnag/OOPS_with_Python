# 19. Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

list_of_lists = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

unique_list = list(set(tuple(lst) for lst in list_of_lists))

unique_list = [list(t) for t in unique_list]

print(unique_list)
