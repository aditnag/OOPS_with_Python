# 11. Write a Python program to sort a dictionary by key.

given_dict = {'banana': 10, 'apple': 5, 'orange': 20, 'kiwi': 3}

keys = list(given_dict.keys())
keys.sort()
asc_dic = {i: given_dict[i] for i in keys}

print(asc_dic)
