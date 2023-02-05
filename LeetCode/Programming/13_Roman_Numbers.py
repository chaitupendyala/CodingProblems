class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        if len(s) == 1:
            return mapping[s]
        sum = 0
        i = 0
        
        while i <= len(s) - 1:
            if i <= len(s) - 2 and ((s[i] == "I" and s[i+1] in ('X', 'V')) or (s[i] == "C" and s[i+1] in ('D', 'M')) or (s[i] == "X" and s[i+1] in ('L', 'C'))):
                sum += mapping[s[i]+s[i+1]]
                i += 2
                continue
            sum += mapping[s[i]]
            i += 1
        return sum