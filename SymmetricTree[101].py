# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

# Example 1:

# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:

# Input: root = [1,2,2,null,3,null,3]
# Output: false

 

# Constraints:

#     The number of nodes in the tree is in the range [1, 1000].
#     -100 <= Node.val <= 100

 
# Follow up: Could you solve it both recursively and iteratively?
# Accepted
# 1.6M
# Submissions
# 2.9M
# Acceptance Rate
# 54.2%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True # возвращаем если дерево симметрично
        return self.isMirror(root.left, root.right) # вызываем функцию сравнения симметрии левой и правой веток

    def isMirror(self, node1, node2):
        if node1 is None and node2 is None: 
            return True # если оба зеркальные 
        if node1 is None or node2 is None: 
            return False # если одна из веток пуста
        if node1.val != node2.val:
            return False # если значение веток не равны
        return self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left) # перебираем левое поддерево первого узла и правое поддерево второго узла, правое поддервео первого узла и левое поддервео второго узла


roots_list = [1,2,2,3,4,4,3],[1,2,2,null,3,null,3]

for i in roots_list:
    Solution.isSymmetric('Success', i)



