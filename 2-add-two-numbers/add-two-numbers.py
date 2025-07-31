# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        tempNode = ListNode(0)
        curr = tempNode
        carry = 0
        while (l1 is not None or l2 is not None or carry is not 0):
            l2_val = l2.val if l2 else 0
            l1_val = l1.val if l1 else 0

            summing = l1_val + l2_val + carry
            carry = summing // 10

            curr.next = ListNode(summing%10)
            curr = curr.next



            if (l1 is not None):
                l1 = l1.next
            if (l2 is not None):
                l2 = l2.next
            
            
        return tempNode.next
        