# 10. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white


class StringOperation:
    def strOpr(self, s):
        ns = sorted(set(s))
        print(ns)


string = list(input().strip().split(","))
obj = StringOperation()
obj.strOpr(string)
