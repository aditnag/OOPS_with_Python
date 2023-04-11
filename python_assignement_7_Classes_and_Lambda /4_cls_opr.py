# 4) Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number. Note: There will be one solution for each input and do not use the same element twice. Input: numbers= [90, 20,10,40,50,60,70], target=50 Output: 3, 4

class Pair:
    def findPair(self, ar, target):
        idx1 = 0
        idx2 = 0
        for i in range(len(ar)):
            if target - ar[i] in ar:
                idx1 = i
                idx2 = ar.index(target - ar[i])
        return (idx1, idx2)


ar = list(map(int, input().strip().split()))
target = int(input("Enter the target: "))
pair = Pair()
print(pair.findPair(ar, target))
