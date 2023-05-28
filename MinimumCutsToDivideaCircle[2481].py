# A valid cut in a circle can be:

# A cut that is represented by a straight line that touches two points on the edge of the circle and passes through its center, or
# A cut that is represented by a straight line that touches one point on the edge of the circle and its center.
# Some valid and invalid cuts are shown in the figures below.


# Given the integer n, return the minimum number of cuts needed to divide a circle into n equal slices.

 

# Example 1:


# Input: n = 4
# Output: 2
# Explanation: 
# The above figure shows how cutting the circle twice through the middle divides it into 4 equal slices.
# Example 2:


# Input: n = 3
# Output: 3
# Explanation:
# At least 3 cuts are needed to divide the circle into 3 equal slices. 
# It can be shown that less than 3 cuts cannot result in 3 slices of equal size and shape.
# Also note that the first cut will not divide the circle into distinct parts.
 

# Constraints:

# 1 <= n <= 100
# Accepted
# 21,862
# Submissions
# 41,773
class Solution(object):
    def numberOfCuts(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n // 2 if n % 2 == 0 else n
#         if n == 1:              # Если n равно 1,
#             return 0            # возвращаем 0, так как не требуется делать никаких разрезов
#         elif n % 2 == 0:        # Если n является четным числом,
#             return n // 2       # возвращаем целочисленное деление n на 2, так как каждый разрез делит круг на две равные части
#         else:                   # В противном случае, когда n является нечетным числом,
#             return n            # возвращаем само n, так как первый разрез не делит круг на разные части

        
    
    
list_n = 4,3
for i in list_n:
    Solution.numberCuts('Success', i)
