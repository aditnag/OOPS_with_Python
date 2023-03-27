# 20. Write a Python program to remove all consecutive duplicates of a given string.

class StringOperation:
    def strOpr(self, string):
        modified_string = ""
        for i in range(len(string)):
            if i == 0 or string[i] != string[i - 1]:
                modified_string += string[i]
        print(modified_string)


string = input("Enter the string: ")
sl = StringOperation()
sl.strOpr(string)
