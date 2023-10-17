# 1290. 
# Easy

# 3975

# 148

# Add to List

# Share
# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.

# The most significant bit is at the head of the linked list.

 

# Example 1:


# Input: head = [1,0,1]
# Output: 5
# Explanation: (101) in base 2 = (5) in base 10
# Example 2:

# Input: head = [0]
# Output: 0
 

# Constraints:

# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.
# Accepted
# 421,489
# Submissions
# 517,482

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        decimal_value = 0
        current = head
        while current:          
            decimal_value = (decimal_value << 1) | current.val
            current = current.next
        return decimal_value


list_h = [1,0,1], [0]

for i in list_h:
   Solution.getDecimalValue('Success', i)
