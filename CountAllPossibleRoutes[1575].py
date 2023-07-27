# 1575. Count All Possible Routes
# Hard

# You are given an array of distinct positive integers locations where locations[i] represents the position of city i. You are also given integers start, finish and fuel representing the starting city, ending city, and the initial amount of fuel you have, respectively.

# At each step, if you are at city i, you can pick any city j such that j != i and 0 <= j < locations.length and move to city j. Moving from city i to city j reduces the amount of fuel you have by |locations[i] - locations[j]|. Please notice that |x| denotes the absolute value of x.

# Notice that fuel cannot become negative at any point in time, and that you are allowed to visit any city more than once (including start and finish).

# Return the count of all possible routes from start to finish. Since the answer may be too large, return it modulo 109 + 7.

 

# Example 1:

# Input: locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5
# Output: 4
# Explanation: The following are all possible routes, each uses 5 units of fuel:
# 1 -> 3
# 1 -> 2 -> 3
# 1 -> 4 -> 3
# 1 -> 4 -> 2 -> 3

# Example 2:

# Input: locations = [4,3,1], start = 1, finish = 0, fuel = 6
# Output: 5
# Explanation: The following are all possible routes:
# 1 -> 0, used fuel = 1
# 1 -> 2 -> 0, used fuel = 5
# 1 -> 2 -> 1 -> 0, used fuel = 5
# 1 -> 0 -> 1 -> 0, used fuel = 3
# 1 -> 0 -> 1 -> 0 -> 1 -> 0, used fuel = 5

# Example 3:

# Input: locations = [5,2,1], start = 0, finish = 2, fuel = 3
# Output: 0
# Explanation: It is impossible to get from 0 to 2 using only 3 units of fuel since the shortest route needs 4 units of fuel.

 

# Constraints:

#     2 <= locations.length <= 100
#     1 <= locations[i] <= 109
#     All integers in locations are distinct.
#     0 <= start, finish < locations.length
#     1 <= fuel <= 200

# Accepted
# 47,384
# Submissions
# 71,011

class Solution:
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

class Solution:
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Инициализируем переменные для отслеживания состояния последовательности и количества изменений
        state = -1 # состояние долины - не определено
        changes_count = 0 # 0 означает уменьшение, 1 означает увеличение.
        
        # Проходимся по элементам массива, начиная с индекса 1, так как нужно сравнивать с предыдущим элементом
        for i in range(1, len(nums)):
            # Если текущий элемент больше предыдущего, последовательность становится возрастающей (hill).
            # Увеличиваем счетчик `changes_count`, если предыдущее состояние было убывающим (state == 0).
            # Затем устанавливаем текущее состояние `state` в 1 (указывает на возрастающую последовательность).
            if nums[i] > nums[i - 1]:
                changes_count += int(state == 0)
                state = 1
            
            # Если текущий элемент меньше предыдущего, последовательность становится убывающей (valley).
            # Увеличиваем счетчик `changes_count`, если предыдущее состояние было возрастающим (state == 1).
            # Затем устанавливаем текущее состояние `state` в 0 (указывает на убывающую последовательность).
            elif nums[i] < nums[i - 1]:
                changes_count += int(state == 1)
                state = 0
        
        # Возвращаем значение счетчика, которое равно количеству холмов и долин
        return changes_count

list_n =  [2,3,6,8,4], [4,3,1], [5,2,1]
for i in list_n:
  Solution.countHillValley('Success', i)
