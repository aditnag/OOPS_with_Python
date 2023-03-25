# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

class StringOperation:
    def strOpr(self, s):
        s = list(s.strip(" "))
        ele = s[0]
        for i in range(1, len(s)):
            if s[i] == ele:
                s[i] = "$"
        for i in range(len(s)):
            print(s[i], end="")


string = input("Enter the string: ")
obj = StringOperation()
obj.strOpr(string)
