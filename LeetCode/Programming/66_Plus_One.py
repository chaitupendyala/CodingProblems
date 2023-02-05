class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits) - 1
        
        while index > 0 and digits[index] == 9:
            digits[index] = 0
            index -= 1

        if index == 0 and digits[0] == 9:
            digits[index] = 1
            digits.append(0)
        else:
            digits[index] += 1
        
        return digits