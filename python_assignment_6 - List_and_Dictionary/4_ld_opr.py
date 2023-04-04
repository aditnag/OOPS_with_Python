# 4. Write a Python script to check if a given key already exists in a dictionary.

key = input("Enter the key: ")
given_dic = {"1": 10, "2": 20, "3": 30, "4": 40, "5": 50, "6": 60}

if key in given_dic:
    print(f"{key} is present")
else:
    print(f"{key} is not present")
