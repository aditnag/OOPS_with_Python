# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

class StringOperation:
    def strOpr(self, s):
        if len(s) > 2:
            if s.endswith("ing"):
                s = s + "ly"
            else:
                s = s + "ing"
            print(s)
        else:
            print(s)


string = input()
obj = StringOperation()
obj.strOpr(string)
