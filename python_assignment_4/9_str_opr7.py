# 9. Write a Python program to remove the nth index character from a nonempty string.

class StringOperation:
    def strOpr(self, s, c):
        first = s[0:c]
        second = s[c+1:]
        print(first+second)


string = input()
ch = int(input())
obj = StringOperation()
obj.strOpr(string, ch)
