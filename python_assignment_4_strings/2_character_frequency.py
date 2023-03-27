# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}


class CharacterFrequency:
    def countCharacterFrequency(self, s):
        charDic = {}
        for i in s:
            if i in charDic:
                charDic[i] += 1
            else:
                charDic[i] = 1
        print(charDic)


string = input("Enter the String: ")
obj = CharacterFrequency()
obj.countCharacterFrequency(string)
