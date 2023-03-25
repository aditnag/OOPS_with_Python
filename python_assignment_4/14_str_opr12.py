# Write a Python program to print the following floating numbers upto 2 decimal places.
# 3.1415926

class StringOperation:
    def strOpr(self, num):
        print(round(num, 2))


f = float(input())
obj = StringOperation()
obj.strOpr(f)
