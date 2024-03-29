# 860. Lemonade Change
# Easy

# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

# Note that you do not have any change in hand at first.

# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

 

# Example 1:

# Input: bills = [5,5,5,10,20]
# Output: true
# Explanation: 
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.

# Example 2:

# Input: bills = [5,5,10,10,20]
# Output: false
# Explanation: 
# From the first two customers in order, we collect two $5 bills.
# For the next two customers in order, we collect a $10 bill and give back a $5 bill.
# For the last customer, we can not give the change of $15 back because we only have two $10 bills.
# Since not every customer received the correct change, the answer is false.

 

# Constraints:

#     1 <= bills.length <= 105
#     bills[i] is either 5, 10, or 20.

# Accepted
# 137,942
# Submissions
# 260,633


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        fiveCount = 0  # Количество доступных купюр номиналом $5
        tenCount = 0  # Количество доступных купюр номиналом $10
    
        for bill in bills:
            if bill == 5:  # Если покупатель платит купюрой номиналом $5
                fiveCount += 1  # Увеличиваем количество $5 купюр на 1
            elif bill == 10:  # Если покупатель платит купюрой номиналом $10
                fiveCount -= 1  # Уменьшаем количество $5 купюр на 1
                tenCount += 1  # Увеличиваем количество $10 купюр на 1
            elif bill == 20:  # Если покупатель платит купюрой номиналом $20
                if tenCount > 0:  # Если у нас есть доступные купюры номиналом $10
                    tenCount -= 1  # Уменьшаем количество $10 купюр на 1
                    fiveCount -= 1  # Уменьшаем количество $5 купюр на 1
                else:  # Если у нас нет доступных купюр номиналом $10
                    fiveCount -= 3  # Уменьшаем количество $5 купюр на 3
    
            if fiveCount < 0 or tenCount < 0:  # Если у нас отрицательное количество купюр
                return False  # Возвращаем False, так как не можем предоставить правильную сдачу
    
        return True  # Если все покупатели получили правильную сдачу, возвращаем True
         
list_b = [5,5,5,10,20], [5,5,10,10,20]
for i in lit_b:
  Solution.lemonadeChange('Success', i)
