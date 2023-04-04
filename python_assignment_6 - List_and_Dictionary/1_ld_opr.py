# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

given_dict = {'apple': 10, 'banana': 5, 'orange': 20, 'kiwi': 3}

sorted_dict = sorted(given_dict.items(), key=lambda x:x[1])
asc_dict = dict(sorted_dict)
print(f"Asc order: {asc_dict}")

sorted_dict = sorted(given_dict.items(), key=lambda x:x[1], reverse=True)
desc_dict = dict(sorted_dict)
print(f"Desc Dict: {desc_dict}")
