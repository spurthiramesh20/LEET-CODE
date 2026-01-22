class Solution(object):
    def romanToInt(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev = 0

        for ch in reversed(s):
            value = roman[ch]
            if value < prev:
                total -= value
            else:
                total += value
            prev = value

        return total


# ---------- TEST ----------
if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("III"))    
    print(sol.romanToInt("IV"))     
    print(sol.romanToInt("IX"))     
    print(sol.romanToInt("LVIII"))  
    print(sol.romanToInt("MCMXCIV"))
