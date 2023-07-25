# 852. Peak Index in a Mountain Array
# Medium

# An array arr a mountain if the following properties hold:

#     arr.length >= 3
#     There exists some i with 0 < i < arr.length - 1 such that:
#         arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#         arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

# Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# You must solve it in O(log(arr.length)) time complexity.

 

# Example 1:

# Input: arr = [0,1,0]
# Output: 1

# Example 2:

# Input: arr = [0,2,1,0]
# Output: 1

# Example 3:

# Input: arr = [0,10,5,2]
# Output: 1

 

# Constraints:

#     3 <= arr.length <= 105
#     0 <= arr[i] <= 106
#     arr is guaranteed to be a mountain array.

# Accepted
# 657,395
# Submissions
# 951,437


class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left, right = 0, len(arr) - 1
        while left < right:
            # Вычисляем индекс середины массива
            mid = left + (right - left) // 2
    
            if arr[mid] < arr[mid + 1]:
                # Если элемент в середине меньше следующего элемента, значит, мы находимся
                # на возрастающем участке, и пик будет справа от mid.
                left = mid + 1
            else:
                # Иначе, если элемент в середине больше следующего элемента, значит,
                # мы находимся на убывающем участке, и пик будет слева от mid.
                right = mid
    
        # В результате работы цикла left и right сойдутся к индексу пика.
        return left


list_a = [0,1,0], [0,2,1,0], [0,10,5,2]
for i in list_a:
   Solution.peakIndexInMountainArray('Success', i)
