# 2) Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
# These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.

class ParenthesisValidator:
    def isValidParenthesis(self, s: str) -> bool:
        stack = []
        param_map = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in param_map.values():
                stack.append(ch)
            elif ch in param_map.keys():
                if not stack or param_map[ch] != stack.pop():
                    return False
            else:
                return False
        return not stack


inp = input()
pv = ParenthesisValidator()
res = pv.isValidParenthesis(inp)
print(res)

