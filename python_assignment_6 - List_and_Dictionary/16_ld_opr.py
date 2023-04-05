# 16. Write a Python program to find the highest 3 values in a dictionary.

dic = {'a': 100, 'b': 200, 'c': 300, 'd': 500, 'e': 900}

sort_dic = sorted(dic.values(), reverse=True)

max_val = sort_dic[:3]

max_keys = [key for key, val in dic.items() if val in max_val]

for key, val in zip(max_keys, max_val):
    print(f"{key} {val}")