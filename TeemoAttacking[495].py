# 495. Teemo Attacking
# Easy

# 1006

# 104

# Add to List

# Share
# Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.

# You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.

# Return the total number of seconds that Ashe is poisoned.

 

# Example 1:

# Input: timeSeries = [1,4], duration = 2
# Output: 4
# Explanation: Teemo's attacks on Ashe go as follows:
# - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
# - At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
# Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.
# Example 2:

# Input: timeSeries = [1,2], duration = 2
# Output: 3
# Explanation: Teemo's attacks on Ashe go as follows:
# - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
# - At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
# Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.
 

# Constraints:

# 1 <= timeSeries.length <= 104
# 0 <= timeSeries[i], duration <= 107
# timeSeries is sorted in non-decreasing order.
# Accepted
# 133,453
# Submissions
# 235,962



class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0  # Возвращаем 0, если массив пустой
    
        total_poisoned_time = 0  # Инициализируем общую длительность отравления
        prev_attack = timeSeries[0]  # Запоминаем время первой атаки
    
        for attack_time in timeSeries[1:]:
            # Вычисляем длительность отравления для текущей атаки, ограниченную 'duration' и временем с момента предыдущей атаки
            poisoned_duration = min(duration, attack_time - prev_attack)
            
            # Добавляем длительность отравления к общей длительности
            total_poisoned_time += poisoned_duration
    
            # Обновляем время предыдущей атаки на текущее время
            prev_attack = attack_time
    
        # Добавляем полную длительность отравления для последней атаки
        total_poisoned_time += duration
    
        return total_poisoned_time


list_nums = [1,4],[1,2]
list_keys = 2,2
 
for index, num in enumerate(list_nums):
    Solution.findPoisonedDuration('Success', num, list_keys[index])
