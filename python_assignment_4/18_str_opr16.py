# 18. Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"

class StringOperation:
    def strOpr(self, s):
        s = s.replace(",", "temp")
        s = s.replace(".", ",")
        s = s.replace("temp", ".")
        print(s)


string = input("Enter the string: ")
sl = StringOperation()
sl.strOpr(string)
