class StrLen:
    def lengthOfString(self, string):
        st = string
        count = 0
        for ch in st:
            count += 1
        print(count)


st = input("Enter the string: ")
sl = StrLen()
sl.lengthOfString(st)
