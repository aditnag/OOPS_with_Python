# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

class StringOperation:
    def strOpr(self, s):
        snot = s.find("not")
        spoor = s.find("poor")
        if spoor > snot > 0 and spoor > 0:
            s = s.replace(s[snot: (spoor + 4)], "good")
            print(s)
        else:
            print(s)


string = input()
obj = StringOperation()
obj.strOpr(string)
