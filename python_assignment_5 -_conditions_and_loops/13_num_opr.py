# 13. Take 10 integers from keyboard using loop and print their average value on the screen.

avg = 0
for i in range(10):
    avg += int(input())
print(avg/10)
