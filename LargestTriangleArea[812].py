# 812. Largest Triangle Area
# Easy

# Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

 

# Example 1:

# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2.00000
# Explanation: The five points are shown in the above figure. The red triangle is the largest.

# Example 2:

# Input: points = [[1,0],[0,0],[0,1]]
# Output: 0.50000

 

# Constraints:

#     3 <= points.length <= 50
#     -50 <= xi, yi <= 50
#     All the given points are unique.

# Accepted
# 43,818
# Submissions
# 72,961

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def calculate_area(p1, p2, p3):
            return 0.5 * abs(p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))
    
        max_area = 0
        n = len(points)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    area = calculate_area(points[i], points[j], points[k])
                    max_area = max(max_area, area)

        return max_area

list_p = [[0,0],[0,1],[1,0],[0,2],[2,0]], [[1,0],[0,0],[0,1]]
for i in list_p:
   Solution.largestTriangleArea('Success', i)




