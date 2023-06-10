# 11. ContainerWithMostWater
# Medium

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:

# Input: height = [1,1]
# Output: 1

 

# Constraints:

#     n == height.length
#     2 <= n <= 105
#     0 <= height[i] <= 104

# Accepted
# 2,134,641
# Submissions
# 3,954,374
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0  # Максимальная площадь контейнера
        left = 0  # Указатель, начинающийся с левого края
        right = len(height) - 1  # Указатель, начинающийся с правого края

        while left < right:
            h = min(height[left], height[right])  # Высота контейнера - минимальная высота из двух линий
            w = right - left  # Ширина контейнера
            area = h * w  # Площадь контейнера
            max_area = max(max_area, area)  # Обновление максимальной площади

            if height[left] < height[right]:  # Перемещение указателя с меньшей высотой
                left += 1
            else:
                right -= 1

        return max_area  # Возвращаем максимальную площадь контейнера
       

    
list_height = [1,8,6,2,5,4,8,3,7],[1,1], [2,2]
fot i in list_height:
   Solution.maxArea('Success', i)
