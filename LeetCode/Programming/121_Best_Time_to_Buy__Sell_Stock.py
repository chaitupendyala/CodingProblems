'''
121. Best Time to Buy and Sell Stock
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different
day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit,
return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
'''
'''
class Solution:
	def maxProfit(self, prices: list[int]) -> int:
		#Kadane's Algorithm - can also be used for max subarray problem
		max_profit = 0
		max_current = 0
		for i in range(1, len(prices)):
			max_current += prices[i] - prices[i-1]
			max_current = max(0, max_current )
			max_profit = max(max_current, max_profit)

		return max_profit
'''
class Solution:
	def maxProfit(self, prices: list[int]) -> int:
		left = 0
		right = 1

		max_profit = 0
		while right < len(prices):
			current_profit = prices[right] - prices[left]

			if ( prices[right] > prices[left] ):
				max_profit = max(max_profit, current_profit)
			else:
				left = right	
			right += 1

		return max_profit

print("prices = [7,1,5,3,6,4]: ", Solution().maxProfit([7,1,5,3,6,4]))
print("prices = [7,6,4,3,1]: ", Solution().maxProfit([7,6,4,3,1]))
print("prices = [7,6,4,3,1]: ", Solution().maxProfit([7,6,4,3,1]))