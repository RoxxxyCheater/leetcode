# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?
# Accepted
# 2M
# Submissions
# 2.6M
# Acceptance Rate
# 73.8%


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    
        # Stack method

        # Создаем пустой стек и пустой список для значений в порядке inorder.
        stack = []
        result = []

        # Идем вглубь дерева, добавляя в стек каждый узел на своем пути.
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            # Как только достигнут конечный узел, добавляем его значение в список,
            # извлекаем его из стека и переходим к его правому поддереву.
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right

        # Возвращаем список значений в порядке inorder.
        return result
    
    
    
    

#           Recursion method

#         if not root:
#             return [] # Отсекаем,если  корень дерева является пустым (null)

#         # Вызываем рекурсивно функцию для левого поддерева,
#         # чтобы получить список значений в порядке inorder.
#         left_values = inorderTraversal(root.left)

#         # Добавляем значение корня в список.
#         root_value = [root.val]

#         # Вызываем рекурсивно функцию для правого поддерева,
#         # чтобы получить список значений в порядке inorder.
#         right_values = inorderTraversal(root.right)

#         # Объединяем все списки и возвращаем их.
#         return left_values + root_value + right_values
    
list_root =  [1,null,2,3], [], [1]
for i in list_root:
   Solution.inorderTraversal('Success', i)
