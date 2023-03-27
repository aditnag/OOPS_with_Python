# 5. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish


n = int(input())
sum = 0
avg = 0
for i in range(n+1):
    sum += i
avg = sum/n
print(f"sum = {sum} and Avg = {avg}")
