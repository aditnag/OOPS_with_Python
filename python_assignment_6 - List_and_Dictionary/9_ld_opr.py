# 9. Write a Python program to multiply all the items in a dictionary.

dic = {'a': 100, 'b': 200, 'c': 300}

p = 1
for i in dic.values():
    p *= i

print(p)
