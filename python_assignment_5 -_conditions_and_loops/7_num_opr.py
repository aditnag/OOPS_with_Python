# 7. Write a Python program that counts the number of elements within a list that are greater than 30.

lst = list(map(int, input().strip().split()))
count = 0
for i in range(len(lst)):
    if lst[i] > 30:
        count += 1

print(f"The number of elements greater than 30 in the list is: {count}")
