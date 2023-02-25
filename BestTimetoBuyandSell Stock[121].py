# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
# Accepted
# 3.1M
# Submissions
# 5.7M
# Acceptance Rate
# 54.3%

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_val,max_val = float('inf'),0
        for price in prices:
            if price < min_val: min_val = price 
            elif price - min_val > max_val: max_val = price - min_val 
        return max_val
   
   
 list_prices = [7,6,4,3,1],[7,1,5,3,6,4]
 for i in list_prices:
    Solution.maxProfit('Success', i)
