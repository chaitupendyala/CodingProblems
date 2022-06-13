'''
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the
two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the
most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7] Output: 49 Explanation: The above vertical lines are represented
by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can
contain is 49. Example 2:

Input: height = [1,1] Output: 1
'''
class Solution:
	def maxArea(self, height: list[int]) -> int:
		numberOfHeights = len(height)
		low = maxArea = 0
		high = numberOfHeights - 1
		if ( numberOfHeights != 0 ):
			while ( low < high ):
				maxArea = max(maxArea, (high - low) * min(height[low],height[high]) )
				if ( height[low] < height[high] ):
					low += 1
				else:
					high -= 1
		return maxArea

print( "[1,8,6,2,5,4,8,3,7]: " + str(Solution().maxArea([1,8,6,2,5,4,8,3,7])) )
print( "[1,1]: " + str(Solution().maxArea([1,1])) )