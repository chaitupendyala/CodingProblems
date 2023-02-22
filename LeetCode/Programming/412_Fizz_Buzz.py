class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = [""]*n
        for i in range(1,n+1):
            found = False
            if i%3 == 0:
                output[i-1] += "Fizz"
                found = True
            if i%5 == 0:
                output[i-1] += "Buzz"
                found = True
            if not found:
                output[i-1] += str(i)
        return output