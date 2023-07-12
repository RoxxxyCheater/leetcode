# 203. Remove Linked List Elements
# Easy

# 7455

# 211

# Add to List

# Share
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

# Example 1:


# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# Example 2:

# Input: head = [], val = 1
# Output: []
# Example 3:

# Input: head = [7,7,7,7], val = 7
# Output: []
 

# Constraints:

# The number of nodes in the list is in the range [0, 104].
# 1 <= Node.val <= 50
# 0 <= val <= 50
# Accepted
# 957,967
# Submissions
# 2,053,656



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        # Создаем фиктивный узел и устанавливаем его следующий узел на голову связного списка
        dummy = ListNode(0)
        dummy.next = head
        
        # Указатель prev указывает на текущий узел, указатель curr указывает на следующий узел
        prev = dummy
        curr = head
    
        # Проходим по связному списку
        while curr:
            # Если значение текущего узла равно val, пропускаем его путем обновления указателей
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            
            # Переходим к следующему узлу
            curr = curr.next
    
        # Возвращаем новую голову связного списка
        return dummy.next


list_h = [1,2,6,3,4,5,6], [], [7,7,7,7]
list_v = 6, 1, 7
for index, num in list_h:
   Solution.removeElements('Success', num, list_v[index])
