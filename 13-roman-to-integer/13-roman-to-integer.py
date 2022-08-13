class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        result = 0

        for n in range(len(s)):
            if n+1 < len(s) and symbols[s[n]] < symbols[s[n+1]]:
                result -= symbols[s[n]]
            else:
                result += symbols[s[n]]
        return result