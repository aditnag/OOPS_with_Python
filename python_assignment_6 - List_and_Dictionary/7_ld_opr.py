# Write a Python script to merge two Python dictionaries

dic1 = {"1": 10, "2": 20}
dic2 = {"3": 30, "4": 40}

# dic_res = dict(dic1.items() | dic2.items())
#
# print(dic_res)

for i in dic2.keys():
    dic1[i] = dic2[i]

print(dic1)
