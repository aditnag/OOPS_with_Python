# 8. Take values of length and breadth of a rectangle from user and check if it is square or not.

l, b = list(map(int, input("Enter length and breadth: ").strip().split()))[:2]
if l == b:
    print("Rectangle is a square")
else:
    print("Rectangle is not a square")