# 10. Write a Python program to remove a key from a dictionary.

dic = {'a': 100, 'b': 200, 'c': 300}

key = input("Enter any a-c key to be removed: ")

if key in dic.keys():
    dic.pop(key)

print(dic)
