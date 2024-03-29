# 2418. Sort the People
# Easy

# You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

# For each index i, names[i] and heights[i] denote the name and height of the ith person.

# Return names sorted in descending order by the people's heights.

 

# Example 1:

# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.

# Example 2:

# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

 

# Constraints:

#     n == names.length == heights.length
#     1 <= n <= 103
#     1 <= names[i].length <= 20
#     1 <= heights[i] <= 105
#     names[i] consists of lower and upper case English letters.
#     All the values of heights are distinct.

# Accepted
# 103,207
# Submissions
# 128,877


class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        # Создаем список кортежей, где каждый кортеж содержит имя и рост одного человека
        person_data = [(name, height) for name, height in zip(names, heights)]
        
        # Сортируем список кортежей по убыванию роста
        person_data.sort(key=lambda x: x[1], reverse=True)
        
        # Создаем список с отсортированными именами из отсортированного списка кортежей
        sorted_names = [name for name, height in person_data]
        
        # Возвращаем отсортированный список имен
        return sorted_names


list_n = ["Mary","John","Emma"], ["Alice","Bob","Bob"]
list_h = [180,165,170], [155,185,150]

for index, n in enumerate('Success'):
  Solution.sortPeople('Success', n, list_h[index])
