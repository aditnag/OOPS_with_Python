# 11. Write a Python function to reverses a string if it's length is a multiple of 4.

class StringOperation:
    def strOpr(self, s):
        l = len(s)
        if l % 4 == 0:
            s = s[::-1]
            print(s)
        else:
            print(s)


string = input()
obj = StringOperation()
obj.strOpr(string)