# 18. From the two list obtained in previous question, make new lists, containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.

lst_even = []
lst_odd = []

for i in range(1, 101):
    if i % 2 == 0:
        lst_even.append(i)
    else:
        lst_odd.append(i)

divisible_by_4 = [n for n in lst_even if n % 4 == 0]
divisible_by_6 = [n for n in range(1, 101) if n % 6 == 0]
divisible_by_8 = [n for n in lst_even if n % 8 == 0]
divisible_by_10 = [n for n in range(1, 101) if n % 10 == 0]
divisible_by_3 = [n for n in range(1, 101) if n % 3 == 0]
divisible_by_5 = [n for n in range(1, 101) if n % 5 == 0]
divisible_by_7 = [n for n in range(1, 101) if n % 7 == 0]
divisible_by_9 = [n for n in range(1, 101) if n % 9 == 0]

for i in divisible_by_4:
    print(i, end=" ")
print()

for i in divisible_by_6:
    print(i, end=" ")
print()

for i in divisible_by_8:
    print(i, end=" ")
print()

for i in divisible_by_10:
    print(i, end=" ")
print()

for i in divisible_by_3:
    print(i, end=" ")
print()

for i in divisible_by_5:
    print(i, end=" ")
print()

for i in divisible_by_7:
    print(i, end=" ")
print()

for i in divisible_by_9:
    print(i, end=" ")
print()