# 12. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

class StringOperation:
    def strOpr(self, s):
        up_count = 0
        for i in s[:4]:
            if i.upper() == i:
                up_count += 1
        if up_count >= 2:
            print(s.upper())
        else:
            print(s)


string = input()
obj = StringOperation()
obj.strOpr(string)