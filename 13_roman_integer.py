class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_value = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        result = 0
        n = len(s)
        for i in range(n) :
            current_value = symbol_value[s[i]]
            if i + 1 < n and current_value < symbol_value[s[i + 1]] :
                result -= current_value
            else :
                result += current_value
        return result 