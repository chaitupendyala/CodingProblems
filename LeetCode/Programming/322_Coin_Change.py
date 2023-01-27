'''
322. Coin Change
Medium

You are given an integer array coins representing coins of different denominations and an integer 
amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
 

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
'''
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        MAX = float('inf')
        OPT = [0] + [MAX] * amount
        for i in range(1, amount + 1):
            OPT[i] = min( [OPT[i-coin] if i - coin >= 0 else MAX for coin in coins] ) + 1
        #print([True, False][1 == 0])
        return [OPT[amount], -1][OPT[amount] == MAX]

print("coins = [1,2,5], amount = 11:", Solution().coinChange(coins = [1,2,5], amount = 11)) #Output: 3
print("coins = [2], amount = 3:", Solution().coinChange(coins = [2], amount = 3)) #Output; -1
print("coins = [1], amount = 0:", Solution().coinChange(coins = [1], amount = 0)) #Output: 0