# 1161. MaximumLevelSumOfABinaryTree
# Medium

# 2994

# 90

# Add to List

# Share
# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

# Example 1:


# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# Example 2:

# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105
# Accepted
# 191,858
# Submissions
# 282,465



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:  # Если корень равен None, то возвращаем 0, так как дерево пустое
            return 0

        queue = deque([(root, 1)])  # Очередь для обхода в ширину, каждый элемент содержит узел и его уровень
        max_sum = float('-inf')  # Максимальная сумма значений, инициализируем с самым маленьким значением
        max_level = 1  # Уровень с максимальной суммой значений, инициализируем как первый уровень

        while queue:  # Пока очередь не пуста
            level_sum = 0  # Текущая сумма значений на уровне
            level_size = len(queue)  # Количество узлов на текущем уровне

            for _ in range(level_size):  # Проходим по всем узлам на текущем уровне
                node, level = queue.popleft()  # Извлекаем узел и его уровень из очереди
                level_sum += node.val  # Добавляем значение узла к текущей сумме уровня

                if node.left:  # Если у узла есть левый потомок, добавляем его в очередь с уровнем на 1 больше текущего
                    queue.append((node.left, level + 1))
                if node.right:  # Если у узла есть правый потомок, добавляем его в очередь с уровнем на 1 больше текущего
                    queue.append((node.right, level + 1))

            if level_sum > max_sum:  # Если текущая сумма значений на уровне больше максимальной суммы
                max_sum = level_sum  # Обновляем максимальную сумму значений
                max_level = level  # Обновляем уровень с максимальной суммой значений

        return max_level  # Возвращаем уровень с максимальной суммой значений

    
list_root = [1,7,0,7,-8,null,null], [989,null,10250,98693,-89388,null,null,null,-32127]
for i in list_root:
  Solution.maxLevelSum('Success', i)
