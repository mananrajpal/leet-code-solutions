from curses.ascii import isalpha, isdigit
from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        chars = list(s)
        brackets = {}
        brackets['('] = ")"
        brackets["{"] = "}"
        brackets["["] = "]"
        
        while len(chars) >= 2:
            end_bracket = chars.pop()
            start_bracket = chars.pop()
            if end_bracket not in brackets or end_bracket != brackets[start_bracket]:
                return False
        return True

sol = Solution()
print(sol.isValid("([)]"))