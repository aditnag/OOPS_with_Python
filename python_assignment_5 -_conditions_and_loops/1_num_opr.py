# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)

class NumOpr:

    def __init__(self, start=1500, end=2700):
        self.start = start
        self.end = end

    def numOpr(self):
        for i in range(self.start, self.end + 1):
            if i % 7 == 0 and i % 5 == 0:
                print(i)


obj = NumOpr()
obj.numOpr()
