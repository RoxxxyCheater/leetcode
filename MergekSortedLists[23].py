# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example 2:

# Input: lists = []
# Output: []

# Example 3:

# Input: lists = [[]]
# Output: []

 

# Constraints:

#     k == lists.length
#     0 <= k <= 104
#     0 <= lists[i].length <= 500
#     -104 <= lists[i][j] <= 104
#     lists[i] is sorted in ascending order.
#     The sum of lists[i].length will not exceed 104.

# Accepted
# 1.6M
# Submissions
# 3.2M
# Acceptance Rate
# 49.6%


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        # Разделяем лист на пополам
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        # рекурсивно соединяем левую и правую сторону списка 
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2: #до последнего элемента
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        return dummy.next
    
lists = [[1,4,5],[1,3,4],[2,6]], [], [[]]
for i in lists:
    Solution.addTwoNumbers('Success', i)