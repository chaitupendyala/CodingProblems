class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(n: str) -> bool:
            if int(n) in visited:
                return False 
            visited.add(int(n))
            sum = 0
            for i in n:
                sum += int(i) ** 2
            if sum == 1:
                return True
            print(sum)
            return happy(str(sum))
        visited = set()
        return happy(str(n))