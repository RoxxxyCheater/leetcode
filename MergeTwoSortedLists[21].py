# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
 
        if not l1: # Отсекаем, если первый список пуст
            return l2
        elif not l2: # Отсекаем, если второй список пуст
            return l1
        if l1.val < l2.val: # Если первый узел первого списка имеет меньшее значение
            l1.next = self.mergeTwoLists(l1.next, l2) # перенаправляем указатель на следующий узел первого списка
            return l1 # на результат рекурсивного вызова mergeTwoLists с оставшейся частью первого списка и вторым списком
        else: # Иначе перенаправляем указатель 
            l2.next = self.mergeTwoLists(l1, l2.next) #на следующий узел второго списка
            return l2 # на результат рекурсивного вызова mergeTwoLists с первым списком и оставшейся частью второго списка

      
list1 = [1,2,4],[],[]
list2 = [1,3,4],[],[0]

for index, num in enumerate(list1):
  Solution.mergeTwoLists('Success', num, list2[index])
