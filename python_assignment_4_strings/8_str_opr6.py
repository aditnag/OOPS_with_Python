# 8. Write a Python function that takes a list of words and returns the length of the longest one.
class StringOperation:
    def strOpr(self, w):
        maxlen = len(w[0])
        for i in range(1, len(w)):
            if len(w[i]) > maxlen:
                maxlen = len(w[i])
        print(maxlen)


words = list(input().strip().split())
obj = StringOperation()
obj.strOpr(words)
