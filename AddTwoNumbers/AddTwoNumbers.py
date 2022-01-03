# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        curr = result
        carry = 0
        while l1 or l2 or carry:
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            val += carry
            carry = val // 10  # float division. ex) 16 // 7 => 2
            val %= 10
            node = ListNode(val=val)
            curr.next = node
            curr = curr.next
        return result.next
