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
