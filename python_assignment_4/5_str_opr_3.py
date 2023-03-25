# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

class StringOperation:
    def str_opr(self, a, b):
        if len(a) > 1 and len(b) > 1:
            c = a + b
            c = list(c.strip(" "))
            for i in range(2):
                temp = c[i]
                c[i] = c[len(a) + i]
                c[len(a) + i] = temp
            for i in range(len(c)):
                print(c[i], end="")
        else:
            print("Ensure the string length is >= 2")


lst = list(map(str, input().strip().split()))[:2]
obj = StringOperation()
obj.str_opr(lst[0], lst[1])
