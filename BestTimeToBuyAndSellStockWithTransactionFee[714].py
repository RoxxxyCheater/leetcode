# 714. Best Time to Buy and Sell Stock with Transaction Fee
# Medium

# 6290

# 166

# Add to List

# Share
# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

# Example 1:

# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# Example 2:

# Input: prices = [1,3,7,5,10,3], fee = 3
# Output: 6
 

# Constraints:

# 1 <= prices.length <= 5 * 104
# 1 <= prices[i] < 5 * 104
# 0 <= fee < 5 * 104
# Accepted
# 277,629
# Submissions
# 412,967


class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        
        # Инициализируем переменные для хранения максимального прибытия при покупке и продаже акций
        buy = -prices[0]  # Максимальная прибыль при покупке акции
        sell = 0  # Максимальная прибыль при продаже акции
        
        for i in range(1, n):
            # Обновляем переменные buy и sell в зависимости от текущей цены акции
            
            # Максимальная прибыль при покупке акции - выбираем между предыдущей максимальной прибылью при покупке и
            # разницей между предыдущей максимальной прибылью при продаже и текущей ценой акции с вычетом комиссии
            buy = max(buy, sell - prices[i])
            
            # Максимальная прибыль при продаже акции - выбираем между предыдущей максимальной прибылью при продаже и
            # суммой предыдущей максимальной прибыли при покупке и текущей цены акции с вычетом комиссии
            sell = max(sell, buy + prices[i] - fee)
        
        return sell

list_prices = [1,3,2,8,4,9],[1,3,7,5,10,3]
list_fee = 2,3
for index, num in enumerate(list_prices):
  Solution.maxProfit('Success', num, list_fee[index])
