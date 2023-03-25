# 13. Write a Python program to check whether a string starts with specified characters.

class StringOperation:
    def strOpr(self, s, ch):
        print(s.startswith(ch))


string = input("Enter the string: ")
ch = input("Enter the specified character: ")
obj = StringOperation()
obj.strOpr(string, ch)

