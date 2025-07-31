# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = []
        while head != None:
            temp.append(head)
            head = head.next
        
        middle = len(temp) // 2

        return temp[middle]
        
        