# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

class StringOperation:
    def strOpr(self, s):
        lst = []
        for i in range(len(s)):
            if s[i] in lst:
                lst.append("$")
            else:
                lst.append(s[i])
        for i in range(len(s)):
            print(lst[i], end="")


string = input("Enter the string: ")
obj = StringOperation()
obj.strOpr(string)
