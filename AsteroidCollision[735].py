# 735. Asteroid Collision
# Medium

# 7116

# 777

# Add to List

# Share
# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

# Constraints:

# 2 <= asteroids.length <= 104
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0
# Accepted
# 391,748
# Submissions
# 865,123

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []  # Инициализируем стек для отслеживания астероидов
    
        for asteroid in asteroids:
            # Если стек пустой или астероид движется вправо, добавляем его в стек
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:
                # Астероид движется влево
                while stack and stack[-1] > 0:
                    top = stack.pop()  # Получаем астероида, двигающегося вправо, из вершины стека
                    if top == -asteroid:
                        # Оба астероида взрываются, если они одинакового размера
                        break
                    elif top > -asteroid:
                        # Астероид, двигающийся вправо, больше, поэтому он выживает
                        stack.append(top)
                        break
                    # Астероид, двигающийся влево, больше, продолжаем проверку
                else:
                    stack.append(asteroid)
    
        return stack

list_a = [5,10,-5], [8,-8], [10,2,-5]
for i in list_a:
   Solution.asteroidCollisiom('Success', i)
