# 17. Write a Python program to convert a string in a list.

class StringOperation:
    def strOpr(self, string):
        string = list(string)
        print(string)


string = input("Enter the string: ")
sl = StringOperation()
sl.strOpr(string)