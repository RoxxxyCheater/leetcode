    
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

# Example 1:


# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:

# Input: head = []
# Output: []
# Example 3:

# Input: head = [1]
# Output: [1]
 

# Constraints:

# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100
# Accepted
# 1,139,498
# Submissions
# 1,828,890

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Если список пуст или содержит только один узел, то нет необходимости менять узлы местами
        if not head or not head.next:
            return head

        # Создаем фиктивный узел, который будет служить новым началом списка
        dummy = ListNode(0)
        dummy.next = head

        # Инициализируем указатели для обмена
        prev = dummy  # Указатель на предыдущий узел
        curr = head  # Указатель на текущий узел

        while curr and curr.next:
            # Узлы, которые нужно поменять местами
            first = curr  # Первый узел
            second = curr.next  # Второй узел

            # Обмен
            prev.next = second
            first.next = second.next
            second.next = first

            # Обновляем указатели для следующей итерации
            prev = first
            curr = first.next

        return dummy.next
        
list_int = [1,2,3,4],[],[1]

for i in list_int:
    Solution.swapPairs('Success', i)
