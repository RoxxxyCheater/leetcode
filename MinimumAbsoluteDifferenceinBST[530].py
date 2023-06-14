# 530. MinimumAbsoluteDifferenceinBST
# Easy

# 2960

# 155

# Add to List

# Share
# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

# Example 1:


# Input: root = [4,2,6,1,3]
# Output: 1
# Example 2:


# Input: root = [1,0,48,null,null,12,49]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 104].
# 0 <= Node.val <= 105
 

# Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# Accepted
# 215,500
# Submissions
# 375,395

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [] 
        prev_val = float('-inf')
        min_diff = float('inf') 
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            min_diff = min(min_diff, abs(node.val - prev_val))
            prev_val = node.val
            
            root = node.right
        
        return min_diff



        # self.min_diff = float('inf')  # Инициализируем минимальную разницу
        
        # def dfs(node, prev_val):
        #     if node is None:
        #         return prev_val
            
        #     # Рекурсивно обходим левое поддерево
        #     prev_val = dfs(node.left, prev_val)
            
        #     # Вычисляем разницу между текущим значением и предыдущим значением
        #     self.min_diff = min(self.min_diff, abs(node.val - prev_val))
            
        #     # Обновляем предыдущее значение
        #     prev_val = node.val
            
        #     # Рекурсивно обходим правое поддерево
        #     prev_val = dfs(node.right, prev_val)
            
        #     return prev_val
        
        # dfs(root, float('-inf'))  # Запускаем обход дерева с начальным значением предыдущего значения
        
        # return self.min_diff
    
list_nums = [4,2,6,1,3],[1,0,48,null,null,12,49] 
for i in list_nums:
  Solution.getMinimumDifference('Success', i)
