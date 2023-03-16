# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:

# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]

# Example 2:

# Input: inorder = [-1], postorder = [-1]
# Output: [-1]

 

# Constraints:

#     1 <= inorder.length <= 3000
#     postorder.length == inorder.length
#     -3000 <= inorder[i], postorder[i] <= 3000
#     inorder and postorder consist of unique values.
#     Each value of postorder also appears in inorder.
#     inorder is guaranteed to be the inorder traversal of the tree.
#     postorder is guaranteed to be the postorder traversal of the tree.

# Accepted
# 511K
# Submissions
# 855K
# Acceptance Rate
# 59.8%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder: # Отсекаем если список inorder пустой
            return None  # дерево пустое
        
        root_val = postorder.pop() # Извлекаем значение корневого узла из postorder
        root = TreeNode(root_val) # Создаем новый узел
        index = inorder.index(root_val) # Находим индекс корневого узла в inorder
        # Разделяем дерево на стороны
        root.right = self.buildTree(inorder[index+1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)
        return root



        # if not postorder: # отсекаем если список постордерного обхода пуст
        #     return None # дерево пустое
        
        # root_val = postorder[-1] # получаем крайний элемент постордерного обхода
        # root = TreeNode(root_val) # Извлекаем корневой узел
        
        
        # root_index = inorder.index(root_val) # получаем индекс корневого узла в инордерном обходе
        
        # # Рекурсивно вызываем функцию для левого поддерева
        # left_inorder = inorder[:root_index]
        # left_postorder = postorder[:root_index]
        # root.left = self.buildTree(left_inorder, left_postorder)
        
        # # Рекурсивно вызываем функцию для правого поддерева
        # right_inorder = inorder[root_index + 1:]
        # right_postorder = postorder[root_index:-1]
        # root.right = self.buildTree(right_inorder, right_postorder)
        
        # return root
    

inorder = [9,3,15,20,7],[-1] 
postorder = [9,15,7,20,3],[-1]

for index,num in enumerate(inorder):
    Solution.countOdds('Success', num, postorder[index])