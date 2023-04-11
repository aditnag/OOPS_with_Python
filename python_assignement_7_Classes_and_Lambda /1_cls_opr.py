# 1) Write a python class to convert an integer into a roman numeral and viceversa

class RomanNumeralConverter:
    def __init__(self):
        self.roman_to_int_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        self.int_to_roman_map = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
                                 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

    def to_roman(self, num: int) -> str:
        if not 1 <= num <= 3999:
            raise ValueError("Input must be between 1 and 3999.")
        result = ""
        for value, numeral in sorted(self.int_to_roman_map.items(), reverse=True):
            while num >= value:
                result += numeral
                num -= value
        return result

    def to_int(self, roman: str) -> int:
        roman = roman.upper()
        result = 0
        i = 0
        while i < len(roman):
            if i + 1 < len(roman) and self.roman_to_int_map[roman[i]] < self.roman_to_int_map[roman[i + 1]]:
                result += self.roman_to_int_map[roman[i + 1]] - self.roman_to_int_map[roman[i]]
                i += 2
            else:
                result += self.roman_to_int_map[roman[i]]
                i += 1
        if self.to_roman(result) != roman:
            raise ValueError("Invalid Roman numeral: {}".format(roman))
        return result


inp = int(input("Enter the number: "))
inp2 = input("Enter the numeral: ")
convert = RomanNumeralConverter()
print(convert.to_roman(inp))
print(convert.to_int(inp2))
