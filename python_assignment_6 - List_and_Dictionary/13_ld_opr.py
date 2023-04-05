# 13. Write a Python program to remove duplicates from Dictionary.

original_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value1', 'key4': 'value3', 'key5': 'value2'}
unique_dict = {}

for key, val in original_dict.items():
    if val not in unique_dict.values():
        unique_dict[key] = val
    else:
        continue

print(unique_dict)

