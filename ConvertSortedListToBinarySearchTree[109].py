# Given the head of a singly linked list where elements are sorted in ascending order, convert it to a
# height-balanced
# binary search tree.

 

# Example 1:

# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

# Example 2:

# Input: head = []
# Output: []

 

# Constraints:

#     The number of nodes in head is in the range [0, 2 * 104].
#     -105 <= Node.val <= 105

# Accepted
# 463.7K
# Submissions
# 774K
# Acceptance Rate
# 59.9%

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """


list_chars = [-10,-3,0,5,9], []
for i in list_chars:
   Solution.isValid('Success', i)