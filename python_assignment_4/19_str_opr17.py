# 19. Write a Python program to find smallest and largest word in a given string.

class StringOperation:
    def strOpr(self, s):
        mins = s
        maxs = ""
        s = list(s.strip(" ").split())
        for i in range(len(s)):
            if len(s[i]) < len(mins):
                mins = s[i]
            if len(s[i]) > len(maxs):
                maxs = s[i]
        print(f"Smallest Word is {mins} and longest word is {maxs}")




string = input("Enter the string: ")
sl = StringOperation()
sl.strOpr(string)