# 14. Write a Python program to check a dictionary is empty or not.

test_dic1 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value1', 'key4': 'value3', 'key5': 'value2'}
test_dic2 = {}

if len(test_dic2) == 0:
    print("Empty Dictionary")
else:
    print("Not Empty")
