class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        sum = ""
        carry = 0
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                sum += str((int(num1[i]) + int(num2[j]) + carry) % 10)
                carry = (int(num1[i]) + int(num2[j]) + carry) // 10
            elif i >= 0:
                sum += str(((int(num1[i]) + carry)) % 10)
                carry  = (int(num1[i]) + carry) // 10
            else:
                sum += str((int(num2[j]) + carry) % 10)
                carry  = (int(num2[j]) + carry) // 10
            j-=1
            i-=1