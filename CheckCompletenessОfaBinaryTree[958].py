# Given the root of a binary tree, determine if it is a complete binary tree.

# In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

# Example 1:


# Input: root = [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
# Example 2:


# Input: root = [1,2,3,4,5,null,7]
# Output: false
# Explanation: The node with value 7 isn't as far left as possible.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 100].
# 1 <= Node.val <= 1000
# Accepted
# 182.3K
# Submissions
# 326.5K
# Acceptance Rate
# 55.8%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:  # Если дерево пустое/полное
            return True
        queue = [root]  # Создаем очередь и добавляем корневой узел в нее
        single_child = False  # узел с одним потомком
        while queue:  # Пока очередь не пуста
            node = queue.pop(0)  # Получаем первый узел
            if node.left:  # Если узел с левым потомком
                if single_child:  
                    return False # Отсекаем узел с одним потомком(дерево не полное)
                queue.append(node.left)  # Добавляем в очередь узел с левым потомком
                if node.right: # Если узел с правым потомком
                    queue.append(node.right) # Добавляем в очередь узел с правым потомком
                else:  # Если узел без правого потомка, то следующие узлы тоже имеют только одного потомка
                    single_child = True
            elif node.right:  # Если узел с правым потомком
                return False # Отсекаем узел с одним потомком(дерево не полное)
            else:  # Если узел без потомков, то следующие узлы тоже имеют только одного потомка
                single_child = True
        return True  # Если после проверки не было найдено узлов с одним потомком, то дерево полное
    
    
roots =[1,2,3,4,5,null,7],[1,2,3,4,5,6]
for i in roots:
    Solution.isCompleteTree('Success', i)
