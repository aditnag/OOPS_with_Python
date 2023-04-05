# 12. Write a Python program to get the maximum and minimum value in a dictionary.
import sys

given_dict = {'banana': 10, 'apple': 5, 'orange': 20, 'kiwi': 3}
max_val = -sys.maxsize
min_val = sys.maxsize

for i in given_dict.values():
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print(f"Max value = {max_val} and Min value = {min_val}")