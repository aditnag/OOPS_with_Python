# 16. Write a Python program to print the index of the character in a string.

class StringOperation:
    def strOpr(self, string):
        for idx, ch in enumerate(string):
            print(f"{idx} - {ch}")


string = input("Enter the string: ")
sl = StringOperation()
sl.strOpr(string)