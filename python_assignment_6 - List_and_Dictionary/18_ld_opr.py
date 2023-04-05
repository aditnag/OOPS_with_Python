# 18. Write a Python program to check if all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

l1 = [{}, {}, {}]
l2 = [{1, 2}, {}, {}]

if all(not d for d in l1):
    print("All dictionaries in the list are empty")
else:
    print("Not all dictionaries in the list are empty")