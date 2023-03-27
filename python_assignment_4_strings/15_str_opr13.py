# 15. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2

class CharacterFrequency:
    def countCharacterFrequency(self, s):
        charDic = {}
        for i in s:
            if i in charDic:
                charDic[i] += 1
            else:
                charDic[i] = 1
        for c in sorted(charDic):
            if charDic[c] > 1:
                print(f"{c} {charDic[c]}")


string = input("Enter the String: ")
obj = CharacterFrequency()
obj.countCharacterFrequency(string)