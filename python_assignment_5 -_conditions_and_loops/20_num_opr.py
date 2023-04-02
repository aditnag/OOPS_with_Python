# 20.You are given with a list of integer elements. Make a new list which will store square of elements of previous list.

n = int(input("Enter the length: "))
int_list = list(map(int, input("Enter list elements: ").strip().split()))[:n]
sq = []
for i in int_list:
    sq.append(i * i)

for i in sq:
    print(i, end=" ")
