# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:

# Input: root = [1,null,2]
# Output: 2

 

# Constraints:

#     The number of nodes in the tree is in the range [0, 104].
#     -100 <= Node.val <= 100

# Accepted
# 2.2M
# Submissions
# 3M
# Acceptance Rate
# 73.6%
# Definition for a binary tree node.
#
# 
# 
# 
#  class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0 
        left_dep = self.maxDepth(root.left) 
        right_dep = self.maxDepth(root.right) 
        return max(left_dep, right_dep) + 1
        
list_nums = [3,9,20,'null','null',15,7] , [1,'null',2]
for i in list_nums:
    Solution.maxDepth('Success', i)